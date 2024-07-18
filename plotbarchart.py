# Chuẩn bị 3 list sau để chuẩn bị vẽ hình:
# not_take_exam_percentage: Phần trăm số người không đăng kí hoặc bỏ thi từng môn
# subjects: Tên các môn học
# not_take_exam: Số người bỏ thi hoặc không đăng kí
#read file
with open ("clean_data.csv", encoding="utf8") as file:
	data = file.read(). split("\n")

header = data[0]
students = data[1:] 
# print(students[0]) will just one line

# remove last student (empty student)
students.pop()

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

#split each student in list
for i in range (len(students)):
	students[i] = students[i].split(",")

# make a list student not take exam according to subjects(index of subs)
not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

#loop through all students without fix them
for student in students:
	# each student iterate through all subjects:
	for i in range (5,16):
		if student[i] == "-1":
			not_take_exam[i-5] += 1 
			# [i-5] is index in not_take_exam list 
# if print this will have error: list index out of range. so must to remove last student above

# make a list of percentage student not take exam 
not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student,2)

#plot the barchart by matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#plot the barchart by matplotlib using 2 list
ax.bar(subjects, not_take_exam_percentage)
# set limit to vertical axis
ax.set_ylim(0,150)

# lable and title
ax.set_ylabel('Percentage')
ax.set_title('Numbers of student who not take an exam')

# Draw number of student on top of each bar
rects = ax.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 2, label, ha="center", va="bottom"
    )

plt.show()
 