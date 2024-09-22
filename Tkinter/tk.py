from tkinter import *
root = Tk() # Dùng root để gọi hàm
root.title("ANH YEU EM LOAN OI") # Tiêu đề
root.resizable(height = True, width = True) # Cho phép thay đổi kích thước
root.minsize(height = 300, width = 400) # Kích thước nhỏ nhất là 300x400
def makecenter(root):
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth() // 2) - (width // 2)
	y = (root.winfo_screenwidth() // 2) - (height // 2)
	root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#makecenter(root)
root.mainloop()