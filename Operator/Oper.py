# Assignment
a = 100
b = float(a)
print("a:",a)
print("b:", b)
c, d, e = 100, "python", 300
print("c, d, e: ", c, d, e)
a, e = e, a
print("a va e sau hoan vi:", a, e)
# Arithmetic
print(e / a)
print(a // e)
print (e % a)
print(2 ** 3)
#Comparsion
print(10 >= 5)
print(10 == 5)
# Logical
print(not(10 > 7))
print((10 > 5) and (7 <= 15))
print((10 < 9) or (1 == 3))
# Indentity 
n = [1, 2, 3]
m = [1, 2, 3]
print(n == m)
print(id(n))
print(id(m))
print(n is m)
# Membership
q = "pham anh kiet"
p = "kiet"
print(p not in q)