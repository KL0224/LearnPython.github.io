# Kiểm tra năm nhuần thông qua số năm nhập vào:
'''
year = int(input("Nhap nam: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print(year, "la nam nhuan")
else:
	print(year, "khong phai nam nhuan")
'''

# Đếm số ngày trong tháng:
'''
month = int(input("Nhap thang: "))
if month in [4, 6, 9, 11]:
	print("Thang {0} co 30 ngay".format(month))
elif month in [1, 3, 5, 7, 8, 10, 12]:
	print("Thang {0} co 31 ngay".format(month))
else:
	year = int(input("Nhap nam: "))
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		print("Thang {0} co 29 ngay".format(month))
	else:
		print("Thang {0} co 28 ngay".format(month))
'''

# Giải phương trình bậc 2:
from math import sqrt
a, b, c = map(float, input("Nhap cac he so a, b, c: ").split())
delta = b**2 - 4*a*c
if delta < 0: 
	print("Phuong trinh vo nghiem")
elif delta == 0:
	x = -b/(2*a)
	print("Phuong trinh co 1 nghiem kep là: x =", x)
else:
	x1 = (-b + sqrt(delta)) / (2 * a)
	x2 = (-b - sqrt(delta)) / (2 * a)
	print("Phuong trinh co 2 nghiem: x1  = {0}, x2 = {1}".format(x1, x2))