# ベトナム高等学校試験 2020 分析
このプロジェクトは、ベトナムの高等学校試験のデータセットを分析することを目的としています。このデータセットには、2020年の試験に関する情報が含まれています。

## 目次
1. [プロジェクト概要](#project-overview)
2. [データ抽出](#data-extraction)
3. [データクリーニング](#data-cleaning)
4. [データ分析](#data-analysis)
5. [可視化](#visualization)
6. [結果](#results)
7. [結論](#conclusion)

## プロジェクト概要 <a class="anchor" id="project-overviewe"></a>
このプロジェクトは以下の主要なステップを含みます：
1. **データ抽出**：公的なウェブサイトからデータを取得する。
2. **データクリーニング**：データの正確性と一貫性を確保する。
3. **データ分析**：データを分析して有意義なインサイトを抽出する。
4. **可視化**：結果を視覚化して傾向やパターンを理解する。

## データ抽出<a class="anchor" id="data-extraction"></a>
データは公的なウェブサイトからCURLを使用して抽出し、クリーニングのために保存しました。

## データクリーニング<a class="anchor" id="data-cleaning"></a>
抽出されたデータは、一貫性を持たせるためにクリーニングされました。クリーニングプロセスには、次のような処理が含まれます：
  - データを個別のレコードに分割
``` 
file = open("raw_data.txt","r")
datas = file.read().split("\n")
```

  - 空のレコードの削除
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

  - 特殊文字の置換
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
```
  - 生年月日の分割
```python
dob_list = dob.split('/')
dd = dob_list[0]
mm = dob_list[1]
yy = dob_list[2]
```
  - スコアの処理
```python
# remove :
scores = scores.replace(":","")
# web error -khxh, khtn has 1 space despite others have 3 spaces. so must change
scores = scores.replace("khxh ", "khxh   ")
scores = scores.replace("khtn ", "khtn   ")
scores = scores.replace(" 10", "  10")
# then split to a list orders to make pairs subject-score
scores_list = scores.split("   ")
data =[name,str(dd),str(mm),str(yy)]
```
## データ分析<a class="anchor" id="data-analysis"></a>

### 試験未受験の分析
* 各科目試験を受けなかった学生の人数を計算し、視覚化しました。
```python
not_take_exam = [0] * len(subjects)
for student in students:
    for i in range(5, 16):
        if student[i] == "-1":
            not_take_exam[i-5] += 1
not_take_exam_percentage = [round(count * 100 / total_student) for count in not_take_exam]
```

### 年齢層別の平均スコア
* 年齢ごとにグループ化し、各年齢層の平均スコアを計算しました。
```python
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
### 受験科目数の分析
* 学生が受けた試験の数とその影響を分析しました。
```python
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

### 人気の苗字
* 学生の中で最も人気のある苗字を特定し、視覚化しました。
```python
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
## 可視化<a class="anchor" id="visualization"></a>
### 試験未受験の割合

```python
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

### 年齢層別の平均スコア
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
### 人気の苗字
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

## 結果<a class="anchor" id="results"></a>

- **試験未受験**: 多くの学生が特定の試験を受けていない割合が顕著でした。
- **平均スコア**: 年齢層ごとに平均スコアにばらつきがありました。
- **受験科目数**: 受験科目数とその平均スコアの影響についてのインサイトが得られました。
- **人気の苗字**: 学生の中で最も一般的な苗字が特定されました。.

## 結論<a class="anchor" id="conclusion"></a>

この分析は、2020年のベトナム高等学校試験を受けた学生のパフォーマンスと人口統計に関するインサイトを提供します。将来的には、さまざまな要因に基づいて学生のパフォーマンスを予測するために機械学習技術を適用することが考えられます。


