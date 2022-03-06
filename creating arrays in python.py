# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:08:06 2022

@author: mon pc
"""

#arrays
#creating an array in python

from array import *
# arrayName=array(typecode, [initializers]) #typecodes define the values which the array will hold
#e.g b represents a signed integer of one byte, B an unsigned obe byte integer, c represents a character of
#one byte, i represents signed integers of two bytes and so on
#initialisers are the elements that would be held in the array

# to work with array module we either work with array or numpy module for example
import array as arr
Array_1 = arr.array('i', [10, 20, 30])
print(Array_1)
print(type(Array_1))

import numpy as np
Array_2 = np.array(['k', 'b'])
print(Array_2)
print(type(Array_2))

