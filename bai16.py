# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:46:54 2024

@author: La Thiên Phụng
"""
gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tonggiay=gio*3600+ phut*60+giay
print("Tổng giây tính được là: ",tonggiay)
