#Most popular Family name in VN? Nguyen?
# Make 2 list: Family name List and numbers of stud have family name appropriate
# sorting decrease 2 list 

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

familyname = []  # list của họ
familyname_count = [] # số lần lặp của họ

for s in students:
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in familyname:
		familyname.append(lastname)
		familyname_count.append(0) # append str 0
		familyname_count[familyname.index(lastname)] +=1
	else:
		familyname_count[familyname.index(lastname)] +=1
# print(familyname)
# print(sum(familyname_count))
#check code
# total = 0
# for s in students:
# 	s_name = s[1].split(" ")
# 	lastname = s_name[0]
# 	if lastname == "Phạm":
# 		total +=1
# print(total)

# sort familyname and familyname_count by decrese
# tại sao cần có 2 vòng lặp vì list counted_max_num sẽ tạo mới ngoài loop j
for i in range(len(familyname_count)):
	for j in range(i +1,len(familyname_count)): # sort từ i +1 để tránh so sánh trùng 
		if familyname_count[i] < familyname_count[j]:
			temp = familyname_count[i]
			familyname_count[i] = familyname_count[j]
			familyname_count[j] = temp

			temp = familyname[i]
			familyname[i] = familyname[j]
			familyname[j] = temp
familyname_count_sorted =familyname_count
familyname_sorted =familyname
# print(familyname_count_sorted)
# print(familyname_sorted)


#plot the most popular 20 family names
import matplotlib.pyplot as plt
import numpy as np
num = 20
x = np.arange(num)
y = np.arange(num)

fig, ax = plt.subplots()

ax.bar(x,familyname_count_sorted[0:num])

#label for column x
plt.xticks(x,familyname_sorted[0:num])

# lable and title
ax.set_ylabel('Numbers of Student')
ax.set_xlabel('FamilyName')
ax.set_title('The most popular'+ str(num)+ 'family names on exam')


# Draw number of student on top of each bar
rects = ax.patches
for rect, label in zip(rects, familyname_count_sorted):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 0.3, label, ha="center", va="bottom"
    )

plt.show()