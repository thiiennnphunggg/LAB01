# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:54:15 2024

@author: La Thiên Phụng
"""
soxe=input("Nhập biển số xe: ")
tong=sum(int(chuso) for (chuso) in (soxe))
hangchuc=tong//10
hangdonvi=tong%10
sonut=hangchuc+hangdonvi
print(f"Vậy xe có {sonut} nút")
