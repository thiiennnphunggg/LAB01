# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:28:37 2024

@author: La Thiên Phụng
"""
#Hình vuông
canh=float(input("Nhập độ dài cạnh hình vuông = "))
p=canh*4
print("Chu vi hình vuông = ",p)
s=canh**2
print("Diện tích hình vuông = ",s)
#Hình chữ nhật
dai=float(input("Nhập chiều dài hình chữ nhật = "))
rong=float(input("Nhập chiều rộng hình chữ nhật = "))
p=(dai+rong)*2
print("Chu vi hình chữ nhật = ",p)
s=dai*rong
print("Diện tích hình chữ nhật = ",s)
#Hình tròn
import math
a=float(input("Bán kính của hình tròn = "))
p=2*math.pi*a
s=a**2*math.pi
print("Chu vi hình tròn = ",p)
print("Diện tích hình tròn = ",s)
