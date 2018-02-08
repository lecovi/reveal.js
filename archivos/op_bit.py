#!/usr/bin/python
# -*- coding: utf-8 -*-

## Operaciones a nivel bit.
## El 4 en binario es 100.
## El 6 en binario es 110.

a = 4
b = 6

## Operador OR:
##     100
##     110
##    -----
##     110
## El resultado de hacer un or binario entre 4 y 6, resulta en 6.
print a | b

## Operador AND:
##     100
##     110
##    -----
##     100
## El resultado de hacer un or binario entre 4 y 6, resulta en 4.
print a & b

## Operador X-OR:
##     100
##     110
##    -----
##     010
## El resultado de hacer un x-or binario entre 4 y 6, resulta en 2.
print a ^ b


## Operador NOT:
##     0100
##    -----
##     1011
## El valor 1011 está en Complemento a 2, por lo tanto, para saber
## el valor que representa, debemos restarle 1 y complementarlo.
##      Por lo tanto el valor es: 1011 - 0001 = 1010.
##      Complementando 1010: 0101, que representa el 5. 
##      En complemento a 2 los números que empiezan con 1 son negativos.
## El resultado de hacer un not binario al 4, resulta en -5.
print ~a

## Desplazar los bits 1 posición a la derecha,
## resulta en: 100 --> 010.
## Entonces el resultado de desplazar 1 posición a la derecha el valor 4, es 2.
## Mover a la derecha resulta en dividir el número en 2^n, donde n es la 
## cantidad de posiciones desplazadas.
print a>>1


## Desplazar los bits 1 posición a la izquierda,
## resulta en: 0100 --> 1000.
## Entonces el resultado de desplazar 1 posición a la izquierda el valor 4, es 8.
## Mover a la izquierda resulta en multiplicar el número en 2^n, donde n es la 
## cantidad de posiciones desplazadas.
print a<<1

