#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:24:33 2019

@author: sean
"""

import numpy as np

test_array = np.zeros((4, 4), dtype=np.bool)
print(test_array)

test_array = np.invert(test_array, dtype=np.bool)
print(test_array)

test_array = np.invert(test_array, dtype=np.bool)
print(test_array)