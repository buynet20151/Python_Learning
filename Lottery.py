# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:35:36 2020

@author: Top
"""

import random
list1=random.sample(range(1,50),7)
special=list1.pop()
list1.sort()
print("本期大樂透中獎號碼為 : ", end="")
for i in range(6):
    if i ==5:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=",")
print("本期大樂透特別號為 :",special)

i = 1
while i % 3: 
    print(i, end = ' ')
    if i >= 10:
        break
    i += 1  