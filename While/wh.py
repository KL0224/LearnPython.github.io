a = 18264914
n = 0
while a > 0:
	n = n*10 + a % 10
	a //= 10
print("So chu so la:", n)
