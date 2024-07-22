{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d9b44a20-2550-4a87-b74f-554820dc40a2",
   "metadata": {},
   "source": [
    "# Vietnam High School Exam 2020 Analysis\n",
    "This project analyzes data from the 2020 high school exams in Vietnam. The primary objectives are to extract, clean, and analyze the data to gain insights into student performance and trends."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6947a47e-0cf5-40d0-b28a-4f805b459fc3",
   "metadata": {},
   "source": [
    "## Table of Contents\n",
    "\n",
    "1. [Project Overview](#project-overview)\n",
    "2. [Data Extraction](#data-extraction)\n",
    "3. [Data Cleaning](#data-cleaning)\n",
    "4. [Data Analysis](#data-analysis)\n",
    "5. [Visualization](#visualization)\n",
    "6. [Results](#results)\n",
    "7. [Conclusion](#conclusion)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e998f645-5ff0-48ca-963b-54ca365be2ec",
   "metadata": {},
   "source": [
    "## Project Overview\n",
    "\n",
    "This project involves several key steps:\n",
    "1. **Data Extraction**: Capturing data from the public website.\n",
    "2. **Data Cleaning**: Ensuring the data is accurate and consistent.\n",
    "3. **Data Analysis**: Analyzing the data to extract meaningful insights.\n",
    "4. **Visualization**: Visualizing the results to better understand trends and patterns."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfb0f9fe-a799-4059-8045-4cc4b9e61949",
   "metadata": {},
   "source": [
    "## Data Extraction\n",
    "\n",
    ">Data was extracted from the public website using CURL. And then put it in file inorder cleaning it\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e17686d-ce64-427c-9822-41d24266d540",
   "metadata": {},
   "source": [
    "## Data Cleaning\n",
    "\n",
    "The extracted data was cleaned to remove inconsistencies and ensure accuracy. This involved (just one individual, for the whole file use for loop functions):\n",
    "\n",
    "- Splitting the data into individual records.\n",
    "```python\n",
    "# Splitting each line in a file  \n",
    "file = open(\"raw_data.txt\",\"r\")\n",
    "datas = file.read().split(\"\\n\")\n",
    "```\n",
    "\n",
    "- Removing empty records.\n",
    " ```python\n",
    "# remove all char \\r and \\t \n",
    "for i in range(len(data)):\n",
    "\tdata[i] = data[i].replace(\"\\\\r\",\"\")\n",
    "\tdata[i] = data[i].replace(\"\\\\t\",\"\")\n",
    "#remove all of tag <>\n",
    "for i in range(len(data)): #loop từng line trong file\n",
    "\tdata[i] = data[i]\n",
    "\ttags = []\n",
    "\tfor j in range(len(data[i])): # loop từng str trong line của file\n",
    "\t\tif data[i][j] == \"<\":\n",
    "\t\t\tbegin = j\n",
    "\t\tif data[i][j] == \">\":\n",
    "\t\t\tend = j\n",
    "\t\t\ttags.append(data[i][begin:end+1])\n",
    "\tfor tag in tags:\n",
    "\t\tdata[i] = data[i].replace(tag, \"\")\n",
    "# remove leading whitespace\n",
    "for i in range(len(data)):\n",
    "\tdata[i] = data[i].strip()\n",
    "# remove empty line\n",
    "unempty_lines = []\n",
    "for i in range(len(data)):\n",
    "\tif data[i] != \"\":\n",
    "\t\tunempty_lines.append(data[i])\n",
    "data = unempty_lines\n",
    "```\n",
    "\n",
    "- Replace special characters in name and scores\n",
    "```python\n",
    "# load unitcode table  \n",
    "chars = []\n",
    "codes = []\n",
    "file = open(\"unicode.txt\", encoding = \"utf8\")\n",
    "unicode_table = file.read().split(\"\\n\")\n",
    "#Split unicode and then replace special characters in name and scores\n",
    "for code in unicode_table:\n",
    "\tx = code.split(\" \")\n",
    "\tchars.append(x[0])\n",
    "\tcodes.append(x[1])\n",
    "for i in range(len(codes)):\n",
    "\tname = name. replace(codes[i], chars[i])\n",
    "\tscores = scores.replace(codes[i], chars[i])\n",
    "# split date of brith\n",
    "dob_list = dob.split('/')\n",
    "dd = dob_list[0]\n",
    "mm = dob_list[1]\n",
    "yy = dob_list[2]\n",
    "# proces scores\n",
    "# remove :\n",
    "scores = scores.replace(\":\",\"\")\n",
    "# web error -khxh, khtn has 1 space despite others have 3 spaces. so must change\n",
    "scores = scores.replace(\"khxh \", \"khxh   \")\n",
    "scores = scores.replace(\"khtn \", \"khtn   \")\n",
    "scores = scores.replace(\" 10\", \"  10\")\n",
    "# then split to a list orders to make pairs subject-score\n",
    "scores_list = scores.split(\"   \")\n",
    "data =[name,str(dd),str(mm),str(yy)]\n",
    "\n",
    "# open new file to check\n",
    "file = open(\"test.txt\", encoding = \"utf8\", mode =\"w\")\n",
    "for i in range(len(data)):\n",
    "\tfile.write(data[i] + \",\")\n",
    "print(data)\n",
    "```\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6b63a82-94a5-4290-9b92-0dd770acfb8b",
   "metadata": {},
   "source": [
    "## Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6c40723-a643-457b-a179-7894b63ce455",
   "metadata": {},
   "source": [
    "### Analyzing Missing Exams\n",
    "\n",
    "The number of students who did not take each subject exam was calculated and visualized. The steps included:\n",
    "- Iterating through each student's records.\n",
    "- Counting the missing exams.\n",
    "- Calculating the percentage of students who did not take each exam."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c693251f-b4b3-4857-84cf-7b126012f2e7",
   "metadata": {},
   "source": [
    "```python\n",
    "# Example code for calculating missing exams\n",
    "not_take_exam = [0] * len(subjects)\n",
    "for student in students:\n",
    "    for i in range(5, 16):\n",
    "        if student[i] == \"-1\":\n",
    "            not_take_exam[i-5] += 1\n",
    "not_take_exam_percentage = [round(count * 100 / total_student) for count in not_take_exam]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63337ebd-0e0d-4f76-8c0f-b9068cccbb5e",
   "metadata": {},
   "source": [
    "### Average Scores by Age Group\n",
    "\n",
    "The average scores were calculated for different age groups. The steps included:\n",
    "- Grouping students by age.\n",
    "- Calculating the average score for each age group.\n",
    "\n",
    "```python\n",
    "# Example code for calculating average scores by age group\n",
    "num_of_student_per_age_group = [0] * 8\n",
    "average_of_student_per_age_group = [0] * 8\n",
    "for student in students:\n",
    "    age = 2020 - int(student[4])\n",
    "    if age >= 24:\n",
    "        age = 24\n",
    "    num_of_student_per_age_group[age - 17] += 1\n",
    "    sum_score = sum(float(student[i]) for i in range(5, 16) if student[i] != \"-1\")\n",
    "    count_score = sum(1 for i in range(5, 16) if student[i] != \"-1\")\n",
    "    if count_score != 0:\n",
    "        average_of_student_per_age_group[age - 17] += sum_score / count_score\n",
    "average_of_student_per_age_group = [avg / num for avg, num in zip(average_of_student_per_age_group, num_of_student_per_age_group)]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06404c1d-f7ad-4223-a15d-8e6a8d68bd1b",
   "metadata": {},
   "source": [
    "### Exam Count Analysis\n",
    "\n",
    "The number of exams taken by students was analyzed. The average score for each number of exams taken was calculated.\n",
    "\n",
    "```python\n",
    "# Example code for calculating exam count analysis\n",
    "num_of_exam_taken = [0] * 12\n",
    "average = [0] * 12\n",
    "for student in students:\n",
    "    count = sum(1 for i in range(5, 16) if student[i] != \"-1\")\n",
    "    total = sum(float(student[i]) for i in range(5, 16) if student[i] != \"-1\")\n",
    "    num_of_exam_taken[count] += 1\n",
    "    if count != 0:\n",
    "        average[count] += total / count\n",
    "average = [avg / num if num != 0 else 0 for avg, num in zip(average, num_of_exam_taken)]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "374085ad-d2d2-4fa9-9912-176d9e13cdf9",
   "metadata": {},
   "source": [
    "### Popular Family Names\n",
    "\n",
    "The most popular family names among students were identified and visualized.\n",
    "\n",
    "```python\n",
    "# Example code for analyzing popular family names\n",
    "familyname = []\n",
    "familyname_count = []\n",
    "for student in students:\n",
    "    lastname = student[1].split(\" \")[0]\n",
    "    if lastname not in familyname:\n",
    "        familyname.append(lastname)\n",
    "        familyname_count.append(1)\n",
    "    else:\n",
    "        familyname_count[familyname.index(lastname)] += 1\n",
    "familyname_count_sorted, familyname_sorted = zip(*sorted(zip(familyname_count, familyname), reverse=True))\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb276aa2-908b-4bbc-ae40-8b8557786457",
   "metadata": {},
   "source": [
    "## Visualization\n",
    "Various visualizations were created using matplotlib to represent the analysis results:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87a61cda-c825-4527-bbf4-9fb4b9d543c1",
   "metadata": {},
   "source": [
    "### Missing Exams Percentage\n",
    "\n",
    "```python\n",
    "# Plotting missing exams percentage\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "fig, ax = plt.subplots()\n",
    "ax.bar(subjects, not_take_exam_percentage)\n",
    "ax.set_ylim(0, 150)\n",
    "ax.set_ylabel('Percentage')\n",
    "ax.set_title('Percentage of Students Not Taking Exams')\n",
    "for rect, label in zip(ax.patches, not_take_exam_percentage):\n",
    "    height = rect.get_height()\n",
    "    ax.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha=\"center\", va=\"bottom\")\n",
    "plt.show()\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5fdcbc3-2f4f-4905-976f-9c2f0f720091",
   "metadata": {},
   "source": [
    "### Average Scores by Age Group\n",
    "\n",
    "```python\n",
    "# Plotting average scores by age group\n",
    "fig, ax = plt.subplots()\n",
    "x = range(8)\n",
    "ax.bar(x, num_of_student_per_age_group)\n",
    "plt.plot(x, average_of_student_per_age_group, color=\"red\", marker=\"o\")\n",
    "ax.set_ylim(0, 70000)\n",
    "ax.set_ylabel('Number of Students')\n",
    "ax.set_xlabel('Age')\n",
    "ax.set_title('Average Scores by Age Group')\n",
    "ax2 = ax.twinx()\n",
    "ax2.tick_params('y', colors=\"r\")\n",
    "ax2.set_ylabel(\"Average Scores\")\n",
    "ax2.set_ylim(0, 10)\n",
    "plt.show()\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d02e5200-06cc-4ddc-856f-b6dda06d1a8e",
   "metadata": {},
   "source": [
    "### Popular Family Names\n",
    "\n",
    "```python\n",
    "# Plotting popular family names\n",
    "fig, ax = plt.subplots()\n",
    "num = 20\n",
    "x = range(num)\n",
    "ax.bar(x, familyname_count_sorted[:num])\n",
    "plt.xticks(x, familyname_sorted[:num])\n",
    "ax.set_ylabel('Number of Students')\n",
    "ax.set_xlabel('Family Name')\n",
    "ax.set_title('Top 20 Most Popular Family Names')\n",
    "for rect, label in zip(ax.patches, familyname_count_sorted[:num]):\n",
    "    height = rect.get_height()\n",
    "    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.3, label, ha=\"center\", va=\"bottom\")\n",
    "plt.show()\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d62a4dde-0fbe-440b-a80d-9f8ef752cf38",
   "metadata": {},
   "source": [
    "## Results\n",
    "\n",
    "- **Missing Exams**: Significant percentages of students did not take certain exams.\n",
    "- **Average Scores**: There were variations in average scores among different age groups.\n",
    "- **Exam Count**: Insights into the number of exams taken and their impact on average scores.\n",
    "- **Popular Names**: Analysis of the most common family names among students."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ee0f868-2811-49ae-aa49-62fbb23356df",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "This analysis provides insights into the performance and demographics of students taking the 2020 high school exams in Vietnam. Future work could involve applying machine learning techniques to predict student performance based on various factors."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
