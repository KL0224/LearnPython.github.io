from math import *
def CheckSNT(n):
	'''Hàm kiểm tra số nguyên tố:'''
	if n < 2:
		return 0
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			return 0
	return 1

#In ra tổng chứ số của n:
def SumChuSo(n):
	s = 0
	while n != 0:
		s += n % 10
		n //= 10
	return s

#In ra tổng chữ số chẵn của n:
def SumChuSoChan(n):
	s = 0
	while n != 0:
		if n % 10 % 2 == 0:
			s += n % 10
		n //= 10
	return s 

#In ra tổng chữ số nguyên tố của n:
def SumChuSoNT(n):
	s = 0
	while n != 0:
		if CheckSNT(n % 10): # n % 10 == 2 or 3 or 5 or 7
			s += n % 10
		n //= 10
	return s 

#In số lật ngược:
def SoNguoc(n):
	nguoc = 0
	while n != 0:
		nguoc = nguoc * 10 + n % 10
		n //= 10
	return nguoc 

#Số lượng thừa số nguyên tố của n:
def SLTSNT(n):
	cnt = 0
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			cnt += 1
			while n % i == 0:
				n //= i
	if n > 1:
		cnt += 1
	return cnt
#In ra thừa số nguyên tố lớn nhất của n:
def TSNTMax(n):
	res = -1
	for i in range(2, isqrt(n) + 1):
		if n % i == 0:
			res = i
		while n % i == 0:
			n //= i
	if n > 1:
		res = n
	return res
#Kiểm tra n có tồn tại ít nhất 1 số 6:
def Check6(n):
	while n != 0:
		if n % 10 == 6:
			return 1
		n //= 10
	return 10

#Kiểm tra tổng chữ số của n chia hết cho 8:
def SumDiv8(n):
	s = SumChuSo(n)
	return s % 8 == 0

#Tính giai thừa của các chữ số:
def GiaiThua(n):
	res = 0
	while n != 0:
		res += factorial(n % 10)
		n //= 10
	return res

# Kiểm tra xem có phải n chỉ được tạo từ 1 số hay không:
def Check1Num(n):
	test = n % 10
	while n != 0:
		if n % 10 != test:
			return False
		n //= 10
	return True

# Kiểm tra chữ số tận cùng lớn nhất:
def CheckMaxDV(n):
	dv = n % 10
	while n != 0:
		if n % 10 > dv:
			return False
		n //= 10
	return True

#In ra tổng lũy thừa của các chữ số của n với số mũ là số chữ số:
def SoChuSo(n):
	cnt = 0
	while n != 0:
		cnt += 1
		n //= 10
	return cnt
def SumLT(n):
	sm = SoChuSo(n)
	s = 0
	while n != 0:
		s += (n % 10)**sm 
		n //= 10
	return s
def Yeu():
	'''Xin chao tat ca cac ban
	Minh la Pham Anh Kiet
	Minh rat thich mot nguoi con gai
	Do chinh la Phan Thi Kim Loan
	Loan anh yeu em nhieu lam
	'''
	print("I love you")
'''
if __name__ == '__main__':
	while True:
		n = int(input("Nhap so n tu ban phim: "))
		if n == 0: break
		if CheckSNT(n):
			print(n, "la so nguyen to")
		else:
			print(n, "khong phai so nguyen to")

		print("Tong cac chu so cua", n, "la:", SumChuSo(n))

		print("Tong chu so chan cua", n, "la:", SumChuSoChan(n))

		print("Tong chu so nguyen to cua", n, "la:", SumChuSoNT(n))

		print("So nguoc cua", n, "la:", SoNguoc(n))

		if Check6(n):
			print(n, "co chu so 6")
		else:
			print(n, "khong co chu so 6")

		if SumDiv8(n):
			print("Tong cac chu so cua", n, "chia het cho 8")
		else:
			print("Tong cac chu so cua", n, "khong chia het cho 8")

		print("Giai thua cua", n, "la:", GiaiThua(n))

		if Check1Num(n):
			print(n, "duoc tao tu mot so")
		else:
			print(n, "khong duoc tao tu mot so")

		if CheckMaxDV(n):
			print("Chu so hang don vi la lon nhat")
		else:
			print("Chu so hang don vi khong phai so lon nhat")

		print("Tong luy thua cua cac chu so cua", n, "la:", SumLT(n))
'''		