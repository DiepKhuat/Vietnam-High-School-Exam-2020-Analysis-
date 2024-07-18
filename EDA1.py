# Hypothesis: Độ tuổi có phản ảnh số điểm không?
# Dựa năm sinh chia nhóm tuổi. loop qua all studs 
# 2 list: list từng nhóm tuổi. đm trung bình từng nhóm tuổi
# line  và bar  để nhìn thấy sự thay đổi theo từng độ tuổi

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
# Get number of student per age group
# 2003 2002 2001 ....1996 under-threshold
num_of_student_per_age_group = [0,0,0,0,0,0,0,0]
average_of_student_per_age_group = [0,0,0,0,0,0,0,0]


for s in students:
	age = 2020 -int(s[4])
	if age >= 24:
		age = 24
	num_of_student_per_age_group[age - 17] += 1

	sum_score = 0
	count_score = 0 # num of exam_taken
	for i in range(11):
		if s[i+5] != "-1":
			count_score += 1
			sum_score += float(s[i+5])
	if count_score != 0:
		averge = sum_score/count_score # avg của tổng các môn thi/ số môn thi
	average_of_student_per_age_group[age- 17] += averge # list avg trên của các nhóm tuổi

for i in range(len(average_of_student_per_age_group)):
	average_of_student_per_age_group[i] = round(average_of_student_per_age_group[i]/ num_of_student_per_age_group[i],2)

# scale-up 1:7
for i in range(len(average_of_student_per_age_group)):
	average_of_student_per_age_group[i] = average_of_student_per_age_group[i]*7000  

# print(num_of_student_per_age_group)
# print(average_of_student_per_age_group)


#plot the barchart by matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(8)
y = np.arange(8)
age_label = [17,18,19,20,21,22,23,24]
fig, ax = plt.subplots()
#plot the barchart by matplotlib using 2 list
ax.bar(x,num_of_student_per_age_group)
#plot line chart
plt.plot(x, average_of_student_per_age_group, color ="red", marker="o")
# set limit to vertical axis
ax.set_ylim(0,70000)

#label for column x
plt.xticks(x,age_label)

# lable and title
ax.set_ylabel('Number of Students')
ax.set_xlabel('Year Olds')
ax.set_title('Average scores according to year olds')

# right side ticks
ax2 = ax.twinx()
ax2.tick_params("y", colors = "r")
ax2.set_ylabel("Average Scores")
ax2.set_ylim(0,10)

# Draw number of student on top of each bar
rects = ax.patches
for rect, label in zip(rects, num_of_student_per_age_group):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 0.3, label, ha="center", va="bottom"
    )

plt.show()