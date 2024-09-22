s = int(input("Chao mung ban den voi python, nhap di: "))
print(s, ":", type(s))

q = input("Nhap 3 so: ")
p = q.split()
a, b, c = map(int , p)
print(a, ":", type(a))
print(b, ":", type(b))
print(c, ":", type(c))
print(a + b + c)

x, y, z, t = map(float, input().split())
print(x + y + z + t)
