#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:41:40 2018

@author: diva
"""

def fahr_to_kelvin(temp):
    ktemp = ((temp-32) * (5/9)) + 273.15
    return(ktemp)
    
def cel_to_fahr(temp):
    return temp*(9/5) + 32
    

if __name__ == "__main__":
    print(fahr_to_kelvin(0))
    print(fahr_to_kelvin(32))
    print(fahr_to_kelvin(100))

    print(cel_to_fahr(0))
    print(cel_to_fahr(100))
