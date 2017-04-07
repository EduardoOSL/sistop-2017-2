coding: utf-8
"""
Stevens Lira Eduardo Orlando
Monitor de Sistema
"""

import threading
import time
import subprocess
hilo=0

Semaforo = threading.Semaphore(1)

def CPU():
  global Semaforo
  Semaforo.acquire()
  print "CPU\n"
  subprocess.call('system_profiler')
  semaforo.release()

def Procesos():
  global Semaforo
  semaforo.acquire()
  print "Procesos actuales\n"
  subprocess.call('ps') 
  Semaforo.release()

def Archivos():
  global Semaforo
  Semaforo.acquire()
  print " Archivos del sistema\n"
  subprocess.call('ls, -a')
  semaforo.release()
  
def Memoria():
  global Semaforo
  Semaforo.acquire()
  print "Memoria\n"
  subprocess.call("vm_stat")
  Semaforo.release()

def Sistema():
  global Semaforo
  Semaforo.acquire()
  print "Arquitectura del sistema\n"
  subprocess.call('arch') 
  print "Versión del Kernel del Sistema\n"
  subprocess.call('uname, -r')
  Semaforo.release()

def Borrar():
  global Semaforo
  semaforo.acquire()
  subprocess.call("clear")
  Semaforo.release()

def Fecha():
  global Semaforo
  semaforo.acquire()
  subprocess.call("date")
  Semaforo.release()

def Lanzador(opcion):
  global hilo
  if (opcion == "Sistema"):
    n=threading.Thread(target = Sistema)
    n.start()
  elif (opcion == "Disco"):
    n=threading.Thread(target = Archivos)
    n.start()
  elif (opcion == "Memoria"):
    n=threading.Thread(target = Memoria)
    n.start()
  elif (opcion == "Proceso"):
    n=threading.Thread(target = Procesos)
    n.start()
  elif (opcion == "CPU"):
    n=threading.Thread(target = CPU)
    n.start()
  elif (opcion == "Fecha"):
    n=threading.Thread(target = Fecha)
    n.start()
  elif (opcion == "Borrar"):
    n=threading.Thread(target = Borrar)
    n.start()
  elif (opcion == "exit"):
    print "Saliendo del sistema"
    hilo=hilo+1
  else:
   print "Opcion invalida"

def hilos():
  s0 = threading.Thread(target = Sistema)
  s0.start()
  s1 = threading.Thread(target = Archivos)
  s1.start()
  s2 = threading.Thread(target = Memoria)
  s2.start()
  s3 = threading.Thread(target = Procesos)
  s3.start()
  s4 = threading.Thread(target = CPU)
  s4.start()
  s5 = threading.Thread(target = Borrar)
  s5.start()
  s6 = threading.Thread(target = Fecha)
  s6.start()

def Monitor():
  global hilo, u, Semaforo
  subprocess.call("clear")
  while t == 0:
      time.sleep(.5)
      print "\tMONITOR\n"
      print "\nSistema\nArchivos\nMemoria\nProcesos\nCPU\nCPU\nBorrar\nFecha\n"
      u = input("Escriba los comandos: ")
      COMMAND(u)
  Semaforo.release()
Monitor()