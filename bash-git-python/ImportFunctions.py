#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:01:45 2018

@author: diva
"""

from FunctionExample import cel_to_fahr

ctemps = [0, 27, 37,16]

for c in ctemps:
    print(cel_to_fahr(c))