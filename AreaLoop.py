#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:35:42 2018

@author: diva
"""

AreaInPixels = 6929
mm2PerPixel = 0.0277

areaInMM = AreaInPixels*mm2PerPixel
print(areaInMM)

areas = [6929.6, 8536.47, 11359.3, 17743.4]


areaInMMlist=[]

for A in areas:
    
    areaInMMlist.append(A*mm2PerPixel)

print(areaInMMlist)
