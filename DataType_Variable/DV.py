# Tính chu vi và diện tích đường tròn khi nhập bán kính:
'''
r = float(input("Nhap ban kinh: "))
cv = 2*3.14*r
dt = 3.14*r*r
print("Chu vi:", cv, "Dien tich:", dt)
'''

# Tính giờ phút giây khi nhập t giây:
'''
t = int(input("Nhap so giay: "))
h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60
print("Thoi gian sau khi quy doi la: {0} gio {1} phut {2} giay".format(h, m, s))
'''

# tính điểm trung bình toán lý hóa với 2 chữ số thập phân:
'''
t = float(input("Nhap diem toan: "))
l = float(input("Nhap diem li: "))
h = float(input("Nhap diem hoa: "))
dtb = (t + l + h) / 3
print("Diem trung binh:", round(dtb, 2))
'''

