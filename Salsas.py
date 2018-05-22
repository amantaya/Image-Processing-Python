#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:03:43 2018

@author: diva
"""

salsas = [['tomatoes', 'onion', 'cilantro', 'jalepeno'], 
          ['mango', 'cucumber', 'jalepeno', 'red onion', 'lime juice'],
          ['avocado', 'lime juice', 'onion', 'salt', 'jalepeno']]
          
print(salsas[0][3])
print(salsas[1][2])
print(salsas[2][-1])

print(salsas[0][3], salsas[1][2], salsas[2][-1])


recipe0 = salsas[0]
print(recipe0)
print(recipe0[3])