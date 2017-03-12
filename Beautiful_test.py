#!/usr/bin/python3
# -*- coding: utf-8 -*-
from func.read_html import read_html

test = read_html('http://himado.in/')
a = test.obj_read()
print(test.read_title())
