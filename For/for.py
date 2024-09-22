from math import *

# Tính S = x + x^2/2! + x^3/3! + ...
'''
def S(x, n):
	s = 0
	for i in range(1, n + 1):
		s += (x**i) / factorial(i)
	return s 
print("S(2, 3) =", S(2, 3))
'''
# Kiểm tra số nguyên tố
'''
def SNT(n):
	if n < 2: 
		return False
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			return False
	return True
while True:
	n = int(input("Nhap n: "))
	if SNT(n):
		print(n, "la so nguyen to")
	else:
		print(n, "khong la so nguyen to")
	s = input("Ban muon tiep tuc khong y/n: ")
	if s == 'n':
		break
'''

# Xuất bảng cửu chương:
'''
for i in range(2, 10):
	print("Bang cuu chuong", i)
	for j in range(1, 11):
		print("{0} * {1} =".format(i, j), i * j)
	print()
'''


