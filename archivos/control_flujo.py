#!/usr/bin/python
# coding: utf-8

## Control de flujo.

## CONDICIONALES
print("CONDICIONALES")
print("="*50)

print("Probemos con un IF solo...(!root)")
user = raw_input("Ingrese su nombre de usuario: " )
if user != "root":
        print("\tUsted no es root, no puede ingresar aquí!")
print("-"*30+"\n")

print("Ahora con una secuencia IF-ELSE... (Leo)")
nombre = raw_input("Ingrese su nombre: ")
if nombre == "Leo":
        print("\tBienvenido LEO!")
else:
        print("\tLárgate de aquí farsante!")
print("-"*30+"\n")

print("Ahora con una secuencia IF-ELIF-ELSE... (0-pos-neg)")
numero = input("Ingrese un número: ")
if numero == 0:
        print("\tUsted ingresó el 0!")
elif numero > 0:
        print("\tEl número ingresado es positivo")
else:
        print("\tEl número ingresado es negativo")
print("-"*30+"\n")

print("Imitando al operador ?.... (par-impar)")
num = input("Ingrese otro número: ")
paridad = "par" if (num % 2 == 0) else "impar"
print("\tEl número ingresado es {}".format(paridad))
print("-"*30+"\n")

raw_input("Presione <enter> para continuar con los ejemplos cíclicos...")

## CÍCLICOS
print("CONDICIONALES")
print("="*50)

print("WHILE")
print("-"*20)
edad = 60
while edad < 65:
        edad = edad + 1
        print("Aún no puede jubilarse, le restan {} años.".format(65-edad))
print("FELICIDADES! Ahora puede disfrutar de su retiro.")
print("-"*30+"\n")

print("BREAK")
print("-"*20)
while True:
        salir = raw_input("Ingrese q para salir o cualquier otra cosa para continuar: ")
        if salir == 'q':
                break
        else:
                print("Continuando")
print("Saliendo...")
print("-"*30+"\n")

print("CONTINUE")
print("-"*20)
print("Imprimiendo número impares...")
n = 0
while n < 30:
        n = n + 1
        if n % 2 == 0:
                continue
        print("{}".format(n))
print("-"*30+"\n")


print("FOR ... IN")
print("-"*20)
iterable = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"]
for elemento in iterable:
        print(elemento)
