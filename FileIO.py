file=open ("dataexam.txt", "w")
# w này là write-mode này tạo file mới overwrite
file.write("ngoc diep\n")
# dùng lệnh này viết vào file data.txt chữ diệp, \n tạo newline char
for i in range (10):
	file.write(str(i) +"\n")

file=open ("dataexam.txt", "r") # read file hiển thị trên terminal
#line = file.read()
# trog máy tính nó hiểu line = "0\n1\n2\n..."

line = file.read().split("\n") 
print(line)
# in ra theo list

# for i in range (10):
# 	print(line[i])
