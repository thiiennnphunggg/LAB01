# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:00:22 2024

@author: La Thiên Phụng
"""
#Giải và biện luận phương trình bậc nhất: ax + b = 0
a=float(input("Nhập a = "))
b=float(input("Nhập b = "))
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Phương trình có nghiệm: ",x)
