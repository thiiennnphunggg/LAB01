# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:25:40 2024

@author: La Thiên Phụng
"""
can_nang=float(input("Nhập cân nặng (kg): "))
chieu_cao=float(input("Nhập chiều cao(m): "))
ktra=can_nang/chieu_cao**2
print("Số đo kiểm tra sức khỏe BMI là: ",ktra)
