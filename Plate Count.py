#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:17:41 2018

@author: diva
"""

count = 207

if count < 30:
    print("count is too small")
elif count < 300:
    print("Plate is countable")
else:
    print("count is too large")

count=207
if count < 30 or count > 300:
    print("Plate is out of range")
else:
    print("Plate is countable")
    
    
