# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:36:36 2024

@author: La Thiên Phụng
"""
ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
#a) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
print(f"{ngay}/{thang}/{nam}")
#b) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90)
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
#c) Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20)
print(f"{nam}/{thang}/{ngay}")
