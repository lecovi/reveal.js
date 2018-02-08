#!/usr/bin/python
# -*- coding: utf-8 -*-

a = True
b = False

print "Para la Suma Lógica:"
print "="*60
print "\tValor 1 \tValor 2 \tSuma"
print "-"*50
print "\t{} \t\t{} \t\t{}".format(a, b, b or b)
print "\t{} \t\t{} \t\t{}".format(a, b, b or a)
print "\t{} \t\t{} \t\t{}".format(a, b, a or b)
print "\t{} \t\t{} \t\t{}".format(a, b, a or a)
print "="*60

print "Para el Producto Lógico:"
print "="*60
print "\tValor 1 \tValor 2 \tProducto"
print "-"*50
print "\t{} \t\t{} \t\t{}".format(a, b, b and b)
print "\t{} \t\t{} \t\t{}".format(a, b, b and a)
print "\t{} \t\t{} \t\t{}".format(a, b, a and b)
print "\t{} \t\t{} \t\t{}".format(a, b, a and a)
print "="*60

print "Para la Negación (o Complemento):"
print "="*60
print "\tValor 1 \tNegación"
print "-"*50
print "\t{} \t\t{}".format(a, not a)
print "\t{} \t\t{}".format(b, not b)
