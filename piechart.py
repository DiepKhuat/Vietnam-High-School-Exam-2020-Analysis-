# Make a list
# num_of_exam_taken - bao nhiêu học sinh thi 0 môn, 1 môn, 2 môn, ....
# piechart sẽ tự đổi danh sách trên thành phần trăm và vẽ hình
with open ("clean_data.csv", encoding = "utf8") as file:
	data = file.read(). split("\n")

header = data[0]
students = data[1:]
total_student = len(students)

header = header.split(",")
subjects = header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")
students.pop()

# numbers of students who took 0,1,2,... subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	count = 0
	for i in range (2):
		if student[i+5] != "-1":
			count += 1
	for i in range (7):
		if student[i+9] != "-1":
			count += 1
	num_of_exam_taken[count] += 1
# check student:
	# if count == 0:
	# 	print(student)

print (sum(num_of_exam_taken))

#pie chart, where the slices will be ordered and plotted counter-clockwise
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

labels = ["0 sub", "1 sub", "2 subs","3 subs", "4","5","6","7","8","9","10","11"]
sizes = np.array([1, 81, 242, 6610, 1171, 26345, 39993, 0, 1, 0, 0, 0])
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.legend()
plt.show() 
plot the barchart by matplotlib



