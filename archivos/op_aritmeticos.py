#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 3
b = 2

## Operador Suma.
c = a + b
print "a vale {}, b vale {} y la suma resulta: {}".format(a, b, c)

## Operador Resta.
c = a - b
print "a vale {}, b vale {} y la resta resulta: {}".format(a, b, c)

## Operador Producto.
c = a * b
print "a vale {}, b vale {} y el producto resulta: {}".format(a, b, c)

## Operador Cociente. 
## Como ambos operandos son enteros, el resultado es entero (trunca el valor).
c = a / b
print "a vale {}, b vale {} y el cociente resulta: {}".format(a, b, c)

## Operador Cociente Entero 
## Como ambos operandos son enteros no hay diferencia con el cociente "común".
c = a // b
print "a vale {}, b vale {} y el cociente entero resulta: {}".format(a, b, c)

## Operador Módulo (devuelve el resto según el cociente de los operandos).
c = a % b
print "a vale {}, b vale {} y el resto resulta: {}".format(a, b, c)

## Operador Exponente.
c = a ** b
print "a vale {}, b vale {} y la potencia resulta: {}".format(a, b, c)

print "-"*15

## Cambiamos el valor de la variable a de entero a real.
print "Convertimos el valor de a de entero a real"
a = float(a)

print "-"*15

## Operador Cociente.
## Como hay un operandos real, el resultado que devuelve es real.
c = a / b
print "a vale {}, b vale {} y el cociente resulta: {}".format(a, b, c)

## Operador Cociente Entero 
## Como hay un operardo real, ahora sí hay diferencia con el cociente "común".
c = a // b
print "a vale {}, b vale {} y el cociente entero resulta: {}".format(a, b, c)

print "="*30

print "Operando con cadenas:"

cadena1 = "Curso"
cadena2 = "Python"

print "Sumando cadenas: {}".format(cadena1+cadena2)

print "Multiplicando cadenas: {}".format(cadena2*5)

