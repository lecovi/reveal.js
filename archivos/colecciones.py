#!/usr/bin/python
# -*- coding: utf-8 -*-

## LISTAS []
## se podría asociar a lo que en otros lenguajes es un array.
## Puede contener cualquier tipo de datos: números, cadenas,
## booleanos ... y también otras listas.
lista = ["Leandro", "Colombo Viña", 32, ["Curso Python", 1]]
print "LISTAS"
print "="*30
print "Viendo el contenido de la lista {}".format(lista)
print "Consultando el primer elemento de la lista: {}".format(lista[0])
print "Consultando el último elemento de la lista: {}".format(lista[-1])
print "\ty dentro de ese, el segundo: {}".format(lista[-1][1])
print "-"*15
print "Cambiando el contenido del primer elemento de la lista..."
lista[0] = "Leandro E."
print "Viendo el contenido de la lista {}".format(lista)
print "="*30

## TUPLAS ()
## similar a las listas.
## Se construyen con ,.
## Son inmutables.
tupla = ("Leandro", "Colombo Viña", 32, ["Curso Python", 1])

print "TUPLAS"
print "="*30
print "Viendo el contenido de la tupla {}".format(tupla)
print "Consultando el primer elemento de la tupla: {}".format(tupla[0])
print "Consultando el último elemento de la tupla: {}".format(tupla[-1])
print "\ty dentro de ese, el segundo: {}".format(tupla[-1][1])
print "-"*15
print "No se puede cambiar el contenido de la tupla!"
## Descomentar la línea siguiente y ejecutar, se puede observar como tira error.
#tupla[0] = "Leandro E."
print "="*30

## DICCIONARIOS {}
## guardan llave - valor.
## No tienen orden!
diccionario = {'nombre': "Leandro", "apellido": 'Colombo Viña', 'edad': 32}
print "DICCIONARIOS"
print "="*30
print "Viendo el contenido del diccionario {}".format(diccionario)
print "Consultando el elemento \'nombre\': {}".format(diccionario['nombre'])
print "Consultando el elemento \'edad\': {}".format(diccionario['edad'])
print "-"*15
print "Cambiando un valor en el diccionario"
## Descomentar la línea siguiente y ejecutar, se puede observar como tira error.
diccionario['edad'] = 25
print "Consultando el elemento \'edad\': {}".format(diccionario['edad'])
print "="*30

