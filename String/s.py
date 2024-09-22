while True:
	s = input("Nhap chuoi de kiem tra: ")
	rev = ''
	for i in range(len(s) - 1, -1, -1):
		rev = rev + s[i]
	print("Chuoi sau khi dao nguoc la:", rev)
	if s == rev:
		print("Chuoi", s, "la chuoi doi xung")
	else:
		print("Chuoi", s, "la chuoi khong doi xung")

	yn = input("Moi ban nhap lua chon co tiep tuc hay khong (y/n): ")
	if yn == 'y':
		print("Moi ban tiep tuc su dung chuong trinh")
	elif yn == 'n':
		print("Ban da chon ket thuc chuong trinh. Tam biet")
		break
	else:
		print("Ba da nhap sai, chuong trinh van hoat dong")
