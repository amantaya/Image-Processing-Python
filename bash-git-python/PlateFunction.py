#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:03:48 2018

@author: diva
"""

import numpy as np

data = np.loadtxt(fname = 'Plates_output_simple.csv', delimiter =',', skiprows = 1, usecols=(3,4,5,6))
