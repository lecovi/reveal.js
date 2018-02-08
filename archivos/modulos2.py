#!/bin/bash/python
# coding: utf-8

import mensajes

## Si queremos omitir el tener que escribir el nombre del
## módulo cuando tenemos que llamar a la función podemos
## utilizar las cláusulas from ... import ...
from mensajes import mensaje1

mensaje1()
print("Esto no es de mensaje, es de módulos2")


