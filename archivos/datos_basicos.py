#!/usr/bin/python
# -*- coding: utf-8 -*-

print("NÚMEROS:")
print "="*30

## NÚMEROS ENTEROS:
## a es una variable entera (long del C).
a = 12
print "a es una variable ", type(a), "y vale: ", a
## b es una variable entera larga.
b = 987L
print "b es una variable ", type(b), "y vale: ", b
## Se puede escribir en octal, anteponiendo un cero.
c = 023
print "c es una variable ", type(c), "y vale: ", c
## O también en hexadecimal, con el prefijo 0x.
d = 0xbc
print "d es una variable ", type(d), "y vale: ", d

print "-"*15

## NÚMEROS REALES:
## e es una variable real (double del C).
e = 3.14
print "e es una variable ", type(e), "y vale: ", e
## Se puede escribir en notación científica.
f = 4.1e-3
print "f es una variable ", type(f), "y vale: ", f

print "-"*15

## NÚMEROS COMPLEJOS:
## g es un número complejo.
g = 3.2 + 8.4j
print "g es una variable ", type(g), "y vale: ", g


print("\nTEXTO:")
print "="*30

## STRINGS:
## cadena es una variable de tipo string.
cadena1 = "Esto es una cadena de texto\n"
print "cadena1 es del tipo ", type(cadena1), "y vale: ", cadena1

## UNICODE:
## Para que la variable almacene el texto en unicode, anteponemos una "u".
cadena2 = u"Esta es una cadena en unicode\n"
print "cadena2 es del tipo ", type(cadena2), "y vale: ", cadena2

## RAW
## Si queremos almacenar una cadena textual (sirve para RegEx), anteponemos una "r".
cadena3 = r"Esta es una cadena cruda\n"
print "cadena3 es del tipo ", type(cadena3), "y vale: ", cadena3

print("\nBOOLEANOS:")
print "="*30
## BOOLEANOS
verdadero = True
falso = False
print "verdadero es una variable de tipo ", type(verdadero), "y vale: ", verdadero
print "falso es una variable de tipo ", type(falso), "y vale: ", falso

print("\nNONE:")
print "="*30
## NONE
ninguno = None
print "ninguno es una variable de tipo ", type(ninguno), "y vale: ", ninguno
