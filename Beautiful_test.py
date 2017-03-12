#!/usr/bin/python3
# -*- coding: utf-8 -*-
from func.get_bs4 import read_soup
import sys

#path = sys.args[1]

test = read_soup('https://en.wikipedia.org/')

bs4_ins = test.bs4obj_ins()
print(test.read_title())
