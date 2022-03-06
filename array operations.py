# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:56:57 2022

@author: mon pc
"""
#arrays and their operations

#creating array
from array import*
num = array('i', [10,20,30,40,50])
for x in num:
    print(x)

#accessing elements of array
print(num[0])
print(num[1])

num.insert(60, 70) #inserting the two elements into the array
print(num)

num.remove(10) #removing element "10" from array
print(num)

print(num.index(50)) #displaying the index of element "50"

num[1] = 80 #updating the element at index  with 80
print(num)

print(type(num))
