def S(n):
	if n == 1:
		return 1
	return n + S(n - 1)

def GT(n):
	if n == 1:
		return 1
	return n * GT(n - 1)
def Fibo(n):
	if n == 0 or n == 1:
		return n
	return Fibo(n - 1) + Fibo(n - 2)
def SumCS(n):
	if n < 10:
		return n
	return n % 10 + SumCS(n // 10)
def nCk(n, k):
	if k == 0 or n == k:
		return 1
	return nCk(n - 1, k - 1) + nCk(n - 1, k)
def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, a % b)
def DectoBin(n):
	if n < 2:
		print(n, end = '')
		return
	DectoBin(n // 2)
	print(n % 2, end = '')
if __name__	== '__main__':
	n = 12
	print(S(n))
	print(GT(n))
	print(Fibo(n))
	print(SumCS(n))
	print(nCk(3, 2))
	print(GCD(6, 4))