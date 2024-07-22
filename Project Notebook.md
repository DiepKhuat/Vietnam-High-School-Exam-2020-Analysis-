# Vietnam High School Exam 2020 Analysis
This project analyzes data from the 2020 high school exams in Vietnam. The primary objectives are to extract, clean, and analyze the data to gain insights into student performance and trends.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Extraction](#data-extraction)
3. [Data Cleaning](#data-cleaning)
4. [Data Analysis](#data-analysis)
5. [Visualization](#visualization)
6. [Results](#results)
7. [Conclusion](#conclusion)

## Project Overview
This project involves several key steps:
1. **Data Extraction**: Capturing data from the public website.
2. **Data Cleaning**: Ensuring the data is accurate and consistent.
3. **Data Analysis**: Analyzing the data to extract meaningful insights.
4. **Visualization**: Visualizing the results to better understand trends and patterns.

## Data Extraction
Data was extracted from the public website using CURL. And then put it in file inorder cleaning it

## Data Cleaning
The extracted data was cleaned to remove inconsistencies and ensure accuracy. This involved (just one individual, for the whole file use for loop functions):
  - Splitting the data into individual records.
```python
# Splitting each line in a file  
file = open("raw_data.txt","r")
datas = file.read().split("\n")
```

  - Removing empty records.
 ```python
# remove all char \r and \t 
for i in range(len(data)):
	data[i] = data[i].replace("\\r","")
	data[i] = data[i].replace("\\t","")
#remove all of tag <>
for i in range(len(data)): #loop từng line trong file
	data[i] = data[i]
	tags = []
	for j in range(len(data[i])): # loop từng str trong line của file
		if data[i][j] == "<":
			begin = j
		if data[i][j] == ">":
			end = j
			tags.append(data[i][begin:end+1])
	for tag in tags:
		data[i] = data[i].replace(tag, "")
# remove leading whitespace
for i in range(len(data)):
	data[i] = data[i].strip()
# remove empty line
unempty_lines = []
for i in range(len(data)):
	if data[i] != "":
		unempty_lines.append(data[i])
data = unempty_lines
```

  - Replace special characters in name and scores
```python
# load unitcode table  
chars = []
codes = []
file = open("unicode.txt", encoding = "utf8")
unicode_table = file.read().split("\n")
#Split unicode and then replace special characters in name and scores
for code in unicode_table:
	x = code.split(" ")
	chars.append(x[0])
	codes.append(x[1])
for i in range(len(codes)):
	name = name. replace(codes[i], chars[i])
	scores = scores.replace(codes[i], chars[i])
# split date of brith
dob_list = dob.split('/')
dd = dob_list[0]
mm = dob_list[1]
yy = dob_list[2]
# proces scores
# remove :
scores = scores.replace(":","")
# web error -khxh, khtn has 1 space despite others have 3 spaces. so must change
scores = scores.replace("khxh ", "khxh   ")
scores = scores.replace("khtn ", "khtn   ")
scores = scores.replace(" 10", "  10")
# then split to a list orders to make pairs subject-score
scores_list = scores.split("   ")
data =[name,str(dd),str(mm),str(yy)]

# open new file to check
file = open("test.txt", encoding = "utf8", mode ="w")
for i in range(len(data)):
	file.write(data[i] + ",")
print(data)
```
## Data Analysis

### Analyzing Missing Exams

The number of students who did not take each subject exam was calculated and visualized. The steps included:
- Iterating through each student's records.
- Counting the missing exams.
- Calculating the percentage of students who did not take each exam.
```python
# Example code for calculating missing exams
not_take_exam = [0] * len(subjects)
for student in students:
    for i in range(5, 16):
        if student[i] == "-1":
            not_take_exam[i-5] += 1
not_take_exam_percentage = [round(count * 100 / total_student) for count in not_take_exam]
```

### Average Scores by Age Group

The average scores were calculated for different age groups. The steps included:
- Grouping students by age.
- Calculating the average score for each age group.

```python
# Example code for calculating average scores by age group
num_of_student_per_age_group = [0] * 8
average_of_student_per_age_group = [0] * 8
for student in students:
    age = 2020 - int(student[4])
    if age >= 24:
        age = 24
    num_of_student_per_age_group[age - 17] += 1
    sum_score = sum(float(student[i]) for i in range(5, 16) if student[i] != "-1")
    count_score = sum(1 for i in range(5, 16) if student[i] != "-1")
    if count_score != 0:
        average_of_student_per_age_group[age - 17] += sum_score / count_score
average_of_student_per_age_group = [avg / num for avg, num in zip(average_of_student_per_age_group, num_of_student_per_age_group)]
```
### Exam Count Analysis

The number of exams taken by students was analyzed. The average score for each number of exams taken was calculated.

```python
# Example code for calculating exam count analysis
num_of_exam_taken = [0] * 12
average = [0] * 12
for student in students:
    count = sum(1 for i in range(5, 16) if student[i] != "-1")
    total = sum(float(student[i]) for i in range(5, 16) if student[i] != "-1")
    num_of_exam_taken[count] += 1
    if count != 0:
        average[count] += total / count
average = [avg / num if num != 0 else 0 for avg, num in zip(average, num_of_exam_taken)]
```

### Popular Family Names

The most popular family names among students were identified and visualized.

```python
# Example code for analyzing popular family names
familyname = []
familyname_count = []
for student in students:
    lastname = student[1].split(" ")[0]
    if lastname not in familyname:
        familyname.append(lastname)
        familyname_count.append(1)
    else:
        familyname_count[familyname.index(lastname)] += 1
familyname_count_sorted, familyname_sorted = zip(*sorted(zip(familyname_count, familyname), reverse=True))
```
## Visualization
Various visualizations were created using matplotlib to represent the analysis results:
### Missing Exams Percentage

```python
# Plotting missing exams percentage
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(subjects, not_take_exam_percentage)
ax.set_ylim(0, 150)
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Students Not Taking Exams')
for rect, label in zip(ax.patches, not_take_exam_percentage):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha="center", va="bottom")
plt.show()
```

### Average Scores by Age Group

```python
# Plotting average scores by age group
fig, ax = plt.subplots()
x = range(8)
ax.bar(x, num_of_student_per_age_group)
plt.plot(x, average_of_student_per_age_group, color="red", marker="o")
ax.set_ylim(0, 70000)
ax.set_ylabel('Number of Students')
ax.set_xlabel('Age')
ax.set_title('Average Scores by Age Group')
ax2 = ax.twinx()
ax2.tick_params('y', colors="r")
ax2.set_ylabel("Average Scores")
ax2.set_ylim(0, 10)
plt.show()
```
### Popular Family Names

```python
# Plotting popular family names
fig, ax = plt.subplots()
num = 20
x = range(num)
ax.bar(x, familyname_count_sorted[:num])
plt.xticks(x, familyname_sorted[:num])
ax.set_ylabel('Number of Students')
ax.set_xlabel('Family Name')
ax.set_title('Top 20 Most Popular Family Names')
for rect, label in zip(ax.patches, familyname_count_sorted[:num]):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.3, label, ha="center", va="bottom")
plt.show()
```

## Results

- **Missing Exams**: Significant percentages of students did not take certain exams.
- **Average Scores**: There were variations in average scores among different age groups.
- **Exam Count**: Insights into the number of exams taken and their impact on average scores.
- **Popular Names**: Analysis of the most common family names among students.

## Conclusion

This analysis provides insights into the performance and demographics of students taking the 2020 high school exams in Vietnam. Future work could involve applying machine learning techniques to predict student performance based on various factors.


