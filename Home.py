# > Imports
import os

# > Inputs
titulo = input("¿Que Titulo quieres asignarle a tu registro?: ")
descripcion = input("Describeme, ¿Que has hecho el dia de hoy?: ")

# > Variables
enter = ""

# > File Generator
Unix = open(f"{titulo}.txt","w")

# > Funciones
if titulo == enter:
	print("Debes agregar un titulo, de lo contrario el programa no funcionara como debe!")
elif titulo != enter:
	Unix.write(descripcion)
	
	
if descripcion == enter:
	print("Debes resumir que has hecho el dia de hoy, de lo contrario, el programa no funcionara como debe!")
elif descripcion != enter:
	Unix.close()
