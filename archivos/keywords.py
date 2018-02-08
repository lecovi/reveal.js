#!/usr/bin/python
# -*- coding: utf-8 -*-

import keyword
print "Python tiene", len(keyword.kwlist), "palabras reservadas:"

for keyword in keyword.kwlist:
        print "\t" + keyword
