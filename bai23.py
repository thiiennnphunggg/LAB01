# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:01:40 2024

@author: La Thiên Phụng
"""
#Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0
import math
a=float(input("Nhập a (khác 0)= "))
b=float(input("Nhập b = "))
c=float(input("Nhập c = "))
delta=b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    x=-b/2*a
    print("Phương trình có nghiệm duy nhất là: ",x)
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("Phương trình có nghiệm x1: ",x1)
    print("Phương trình có nghiệm x2: ",x2)
