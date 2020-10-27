#Unix Properties
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
cprint(figlet_format("Unix", font="doh"), "blue") #Usando una funcion de colorama llamada cprint para imprimir un texto ascii en color usando la funciones de pyfiglet
import os
import errno

# > inputs
titulo = input("¿Que titulo deseas usar?: ")            #Solicitando un titulo de archivo
descripcion = input("¿Que deseas comentar?: ")          #Solicitando una descripcion del archivo
namedir = input("Ingrese el nombre de la ruta: ")       #Solicitando una ruta donde quiere almacenar el archivo

# > Condiciones
if titulo == "":
    print("Debes asignarle un titulo a tu archivo")
elif titulo == " ":
    print("Debes asignarle un titulo a tu archivo")
elif descripcion == "":
    print("Debes asignar una descricion")
elif descripcion == " ":
    print("Debes asignar una descricion")
elif namedir == "":
    print("Debes asignarle un nombre al directorio")
elif namedir == " ":
    print("Debes asignarle un nombre al directorio")
else:
    os.mkdir(namedir)
    Unix = open(f"c:{namedir}\{titulo}.txt", "w")
    Unix.write(descripcion)
    Unix.close()
