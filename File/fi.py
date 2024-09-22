def file(path1, path2):
	file1 = open(path1, 'r', encoding = 'utf-8')
	file2 = open(path2, 'w', encoding = 'utf-8')
	for line in file1:
		data = line.strip()
		file2.writelines(data)
		file2.writelines('\n')
	file1.close()
	file2.close()
file('input.txt', 'output.txt')