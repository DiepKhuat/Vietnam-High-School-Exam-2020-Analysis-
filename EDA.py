# average scores according to subjects were be taken
# Hypothesis : Toán và Văn bắt buộc nhưng sao Có phải điểm kém mà bỏ thi không?
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
average = [0,0,0,0,0,0,0,0,0,0,0,0]

for student in students:
	count = 0
	total = 0 # total scores of subs
	for i in range (11):
		if student[i+5] != "-1":
			total += float(student[i+5]) 
			count += 1
	num_of_exam_taken[count] += 1
	if count != 0:
		average[count] += total/count   # total_average of taken exam

for i in range(12):
	if num_of_exam_taken[i] != 0:
		average[i] = round (average[i]/ num_of_exam_taken[i],2)

print(num_of_exam_taken)
print(average)
#plot the barchart by matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)
fig, ax = plt.subplots()
#plot the barchart by matplotlib using 2 list
ax.bar(x,average)
# set limit to vertical axis
ax.set_ylim(0,10)

#label for column x
plt.xticks(x,y)

# lable and title
ax.set_ylabel('Average Score')
ax.set_title('Average scores according to subjects')

# Draw number of student on top of each bar
rects = ax.patches
for rect, label in zip(rects, average):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 0.3, label, ha="center", va="bottom"
    )

plt.show()
