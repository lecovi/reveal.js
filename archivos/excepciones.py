#!/usr/bin/python

variable = input("1° Caso) Ingrese un número: ")

try:
    numero = int(input("2° Caso) Ingrese otro número: "))
except Exception as err:
    print(f"Ha ocurrido un error: {err}")
else:
    print(f"Usted ingresó {variable} y {numero}")
finally:
    print("Se terminó el programa, limpiando...")