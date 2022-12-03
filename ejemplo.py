#VARIABLES GLOBALES
primerIzquierdo = True
primerDerecho = True
primerArriba = True
primerAbajo = True
XSEMAFORO = 6
YSEMAFORO = 9
CERO = 0
QUINCE = 15
SIETE = 7
OCHO = 8
SEIS = 6
NUEVE = 9

# Model design
import random
import agentpy as ap
import numpy as np

# Visualization
import matpltlib.pyplot as plt
import IPython
from random import choice
from IPython.display import HTML

def funcionVacia():
  return True

def SemaforoSeisSeis(inicioX, inicioZ):
  global SEIS
  if(inicioX==SEIS and inicioZ==SEIS ):
    return True
  else:
    return False

def SemaforoSeisNueve(inicioX, inicioZ):
  global SEIS, NUEVE
  if(inicioX==SEIS and inicioZ==NUEVE ):
    return True
  else:
    return False

def SemaforoNueveNueve(inicioX, inicioZ):
  global NUEVE
  if(inicioX==NUEVE and inicioZ==NUEVE ):
    return True
  else:
    return False

def SemaforoNueveSeis(inicioX, inicioZ):
  global NUEVE, SEIS
  if(inicioX==SEIS and inicioZ==NUEVE ):
    return True
  else:
    return False

def llenarTuplaPosicionesCarros(cCarros):
  global SIETE, OCHO, CERO, QUINCE
  contador = 0
  origenes = [(CERO, SIETE), (OCHO,CERO), (SIETE,QUINCE), (QUINCE,OCHO)]
  tupla=[]
  while(contador!=cCarros):
    tupla.append(random.choice(origenes))
    contador=contador+1
  return tupla

def carroIzquierda(inicioX, inicioZ, condicion):
  global OCHO, CERO, QUINCE
  if(inicioX==QUINCE and inicioZ==OCHO and condicion!=CERO):
    return True
  else:
    return False

def carroDerecha(inicioX, inicioZ, condicion):
  global SIETE, CERO, QUINCE
  if(inicioX==CERO and inicioZ==SIETE and condicion!=QUINCE):
    return True
  else:
    return False

def carroArriba(inicioX, inicioZ, condicion):
  global OCHO, CERO, QUINCE
  if(inicioX==OCHO and inicioZ==CERO and condicion!=QUINCE):
    return True
  else:
    return False

def carroAbajo(inicioX, inicioZ, condicion):
  global SIETE, CERO, QUINCE
  if(inicioX==SIETE and inicioZ==QUINCE and condicion!=CERO):
    return True
  else:
    return False

class agenteSemaforo(ap.Agent):
  def setup (self):
    self.grid = self.model.grid