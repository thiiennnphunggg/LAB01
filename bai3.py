# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:07:10 2024

@author: La Thiên Phụng
"""
a = int(input("Nhập số nguyên dương a = "))  
b = int(input("Nhập số nguyên dương b = "))  
if a>0 and b>0:
    chia_lay_du=a%b
    chia_lay_nguyen=a//b
    print("Phần dư của a chia cho b là: ",chia_lay_du)
    print("Phần nguyên của a chia cho b là: ",chia_lay_nguyen)
