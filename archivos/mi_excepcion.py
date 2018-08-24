#!/usr/bin/python


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
        
    def __str__(self):
        return f"Error: {self.valor}"


try:
    valor = input("Ingrese un número:")
    if valor > 0:
        raise MiError("Ingresó un número positivo!")
except MiError as e:
    print(e)

print("Programa finalizado")
