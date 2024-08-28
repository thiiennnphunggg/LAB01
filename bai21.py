# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:58:53 2024

@author: La Thiên Phụng
"""
S=int(input("Nhập số bất kì: "))
so_chuoi={0:"Không",1:"Một",2:"Hai",3:"Ba",4:"Bốn",5:"Năm",6:"Sáu",
          7:"Bảy",8:"Tám", 9:"Chín"}
if 0<=S<=9 :
    print(so_chuoi[S])
else:
    print("Không đọc được")
