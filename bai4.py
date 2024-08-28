# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:09:14 2024

@author: La Thiên Phụng
"""
N=int(input("Nhập N = "))
chu_so_1=N//10
chu_so_2=N%10
tong=chu_so_1+chu_so_2
if 10 <= N <= 99:
    print("Tổng = ",tong)
else:
    print("Không hợp lệ ")
