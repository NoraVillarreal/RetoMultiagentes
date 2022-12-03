from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import logging

from traffic_model import TrafficModel

model = TrafficModel(16, 10, 10, 1)

def updatePositions():
  model.step()
  positions = model.ps
  return positions

# función que pone las coordenadas de cada agente en un JSON (diccionario)
def positionsToJSON(ps):
  posDICT = []
  for p in ps:
    pos = {
      'x': p[0],
      'z': p[1]
    }
    posDICT.append(pos)
  return json.dumps(posDICT)

class positionHandler(BaseHTTPRequestHandler):
  def _set_response(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def do_GET(self):
    logging.info("GET request, \nPath: %s\nHeaders:\n%s\n", str(self.path),
                 str(self.headers))
    positions = updatePositions()
    self._set_response()
    resp = "{\"data\":" + positionsToJSON(positions) + "}"
    self.wfile.write(resp.encode('utf-8'))

def main():
  PORT = 8001
  server = HTTPServer(('', PORT), positionHandler)
  print('Server running on port %s' % PORT)
  server.serve_forever()
  # ctrl + C para detener el servidor

if __name__ == '__main__':
  main()