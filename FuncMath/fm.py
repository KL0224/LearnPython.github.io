from random import randrange
from math import *

# Game đoán số:
'''
cnt = 0
while True:
	n = int(input("Nhap so ban doan: "))
	number = randrange(1, 101)
	print("So ngau nhien:", number)
	cnt += 1
	if n == number:
		print("Ban da doan dung so. Ban da chien thang")
	elif cnt == 7: 
		print("Ban da doan sai 7 lan. Do do chuong trinh sẽ ket thuc")
		break
	else:
		print("Ban da doan sai, ban da doan sai {0} lan, moi ban doan lai".format(cnt))
'''

# Kiểm tra tính hợp lệ của tam giác và tính diện tích
'''
a, b, c = map(float, input("Moi nhap ba canh cua tam giac: ").split())
if a + b > c and a + c > b and b + c > a:
	print("Tam giac hop le")
	cv = a + b + c
	p = cv / 2
	dt = sqrt(p * (p - a) * (p - b) * (p - c))
	print("Dien tich tam giac:", dt)
else:
	print("Tam giac khong hop le")
'''

# Tính điểm trung bình
'''
t, l, h = map(float, input("Nhap 3 diem toan li hoa: ").split())
print("Diem trung binh:", round((t + l + h) / 3, 2))
'''