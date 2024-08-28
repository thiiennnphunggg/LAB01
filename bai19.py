# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:54:23 2024

@author: La Thiên Phụng
"""
a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
d=int(input("Nhập d = "))
#Giả định số nhỏ nhất là a
sonhonhat=a
if b<sonhonhat:
    sonhonhat=b
if c<sonhonhat:
    sonhonhat=c
if d<sonhonhat:
    sonhonhat=d
print("Số nhỏ nhất là: ",sonhonhat)
