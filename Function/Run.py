# Tính chỉ số BMI
'''
def BMI(w, h):
	bmi = w / (h*h)
	print("Chi so BMI la:", bmi)
	if bmi < 18.5:
		print("Phan loai: Gay")
		print("Nguy co phat trien benh: thap")
	elif bmi < 25:
		print("Phan loai: Binh thuong")
		print("Nguy co phat trien benh: trung binh")
	elif bmi < 30:
		print("Phan loai: Hoi beo")
		print("Nguy co phat trien benh: cao")
	elif bmi < 35:
		print("Phan loai: Beo phi cap do 1")
		print("Nguy co phat trien benh: cao")
	elif bmi < 40:
		print("Phan loai: Beo phi cap do 2")
		print("Nguy co phat trien benh: rat cao")
	else:
		print("Phan loai: Beo phi cap do 3")
		print("Nguy co phat trien benh: nguy hiem")

while True:
	w, h = map(float, input("Nhap can nang(kg) va chieu cao(h): ").split())
	BMI(w, h)
	s = input("Moi nhap lua chon co tiep tuc hay khong (y/n): ")
	if s == 'n': break
'''

# Tính ROI
'''
def ROI(dt, cp):
	return (dt - cp) / cp
	
dt, cp = map(float, input("Nhap doanh thu va chi phi: ").split())
roi = ROI(dt, cp)
print("Ty le ROI:", roi)
print("Dau tu") if roi >= 0.75 else print("Khong dau tu")
'''

# Tính fibonacci
'''
def fibo(n):
	if n == 0 or n == 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

print(fibo(6))
'''