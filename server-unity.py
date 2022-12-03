# Servidor python para la comunicación con Unity

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import numpy as np

import ejemplo.py  # agentes

# Tamaño del grid:
width = 10
height = 10

parameters = {
  'size': 16,
  'carros': 6,
  'semaforos': 2,
  'steps': 200,
}

model = ejemplo.claseModelo(parameters)  # REEMPLAZAR CON ARCHIVO MODEL
model.setup()


def updatePositions():
  model.step()
  positions = model.getPosition()
  return positions


# función que pone las coordenadas de cada agente en un JSON (diccionario)
def positionsToJSON(ps):
  posDICT = []
  for p in ps:
    pos = {
      'x': p[0],
      'z': p[1],
      'y': 0.5  # cambiar altura conforme sea necesario
    }
    posDICT.append(pos)
  return json.dumps(posDICT)


class Server(BaseHTTPRequestHandler):

  def _set_response(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    logging.info("GET request, \nPath: %s\nHeaders:\n%s\n", str(self.path),
                 str(self.headers))
    self._set_response()
    self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    # post_data = self.rfile.read(content_length)
    post_data = json.loads(self.rfile.read(content_length))
    #logging.info("POST request, \nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
    logging.info("POST request, \nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                 str(self.path), str(self.headers), json.dumps(post_data))

    # actualiza información
    positions = updatePositions()
    self._set_response()
    # HAY QUE AGREGAR EL CÓDIGO PARA HACER EL JSON DENTRO DE STEP()
    resp = "{\"data\":" + positionsToJSON(positions) + "}"

    self.wfile.write(resp.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=8585):
  logging.basicConfig(level=logging.INFO)
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  logging.info("Starting httpd...\n")  #HTTPD = HTTP Daemon
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:  # ctrl+C detiene el servidor
    pass
  httpd.server_close()
  logging.info("Stopping httpd...\n")

if __name__ == '__main__':
  from sys import argv

  if len(argv) == 2:
    run(port=int(argv[1]))
  else:
    run()
