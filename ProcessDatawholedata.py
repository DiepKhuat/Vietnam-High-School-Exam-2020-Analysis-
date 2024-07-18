import csv

file = open("raw_data.txt","r")
# Read whole file by split for each student
datas = file.read().split("\n")
#func with: will open file and then code end the file will close. also can use file =open
with open("clean_data.csv", encoding = "utf8", mode ="w", newline="") as file_csv:
	header = ["sbd", "tên","dd", "mm", "yy","toán", "ngữ văn", "khxn", "khtn", "lịch sử", "địa lý", "gdcd", "sinh học","vật lí", "hóa học", "tiếng anh"]
	writer = csv.writer(file_csv)
	writer.writerow(header)

 
sbd = 2000000
# if not open a new file, frist stu will be doubled
# then put it in for loop
for data in datas:
	sbd += 1
	if sbd in [2000521,2002776,2002833,2005380,2005472,2005733,2005820,2005876,2006091,2006300,2006364,2006544,2006712,2006720,2006904,2008746,2009196,2012503,2019593,2020755,2024536,2027212,2031588,2031948,2035434,2036693,2042067,2042972,2043577,2044668,2046177,2046483,2046496,2046651,2046766,2046771,2046788,2046810,2046841,2046998,2047031,2047122,2047241,2047273,2047304,2047486,2047636,2047834,2047843,2047856,2047865,2048225,2048271,2048279,2048397,2048424,2048427,2048592,2048660,2048701,2048723,2048858,2049069,2049090,2049104,2049164,2049234,2049312,2049383,2049663,2049763,2049775,2049891,2049971,2050378,2050476,2050488,2050516,2050526,2050540,2050576,2050642,2050649,2050722,2050809,2050814,2050899,2050959,2050978,2050984,2050985,2051006,2051072,2051181,2051191,2051234,2051422,2051468,2051472,2051495,2051615,2051616,2051736,2052013,2052030,2052089,2052314,2052373,2052591,2052663,2052711,2052791,2052856,2053000,2053106,2053259,2053593,2053699,2053860,2054235,2054306,2054374,2054508,2054733,2054787,2055119,2055200,2055290,2055296,2055606,2055683,2055803,2055829,2055912,2055930,2055986,2056020,2056032,2056105,2056139,2056186,2056190,2056238,2056273,2056291,2056298,2056333,2056350,2056377,2056393,2056782,2056823,2056865,2056871,2057014,2057294,2057410,2057496,2058404,2058498,2058518,2058789,2058938,2059095,2059163,2059740,2059751,2059769,2059774,2059807,2059852,2060462,2060492,2060536,2060610,2060652,2060656,2060660,2060730,2060738,2061813,2062212,2062236,2062391,2062440,2062898,2063109,2063114,2063179,2063180,2063181,2063207,2063272,2063653,2063707,2063716,2063752,2063754,2063825,2064369,2064704,2064783,2064990,2065104,2065323,2065604,2065877,2065995,2066106,2066212,2066835,2067172,2067291,2067316,2067371,2067383,2067401,2067446,2067467,2067550,2067563,2067659,2067672,2067698,2067762,2067909,2067971,2067996,2068089,2068119,2068156,2068174,2068178,2068243,2068287,2068365,2068382,2068427,2068453,2068548,2068550,2068627,2068667,2068702,2068732,2068846,2068970,2069028,2069043,2069066,2069156,2069290,2069362,2069397,2069843,2069990,2070203,2070870,2071102,2071574,2072480,2072549,2072755,2072823,2073036,2073372,2073477,2073556,2073964,2074135,2074254,2074281,2074367,2074607,2074719]:
		continue
	sbd_str = "0" + str(sbd)
	# make each student data becomes a list
	data = data.split("\\n")

	# remove all char \r and \t cz its mean nothing 
	# cz \n is specical char so have to use \\n
	for i in range(len(data)):
		data[i] = data[i].replace("\\r","")
		data[i] = data[i].replace("\\t","")


	#remove all of tag <>. Cách execute:
	# a = '<script src=>sobaodanh</script>'
	# b = []
	# for i in range(len(a)): # i is index, vs mỗi 1 vị trí- và fai lặp vs len của str
	# 	if a[i] == "<":
	# 		begin = i
	# 	if a[i] == ">":
	# 		end = i
	# 		b.append(a[begin:end+1])

	# for ele in b: # loop vs từng element trong list mà ko cần use len()
	# 	a = a.replace(ele,"")
	# # code trên:vs từng elements xác định trong list b, ta sẽ xóa nó ra khỏi a
	# print(a)
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

	# choose neccessary(relevant) inform - công đoạn debug
	name = data[7]
	dob = data[8]
	scores = data[9]


	# cách tạo unicode.text là search ký tự tự đb lên gg r cop unit8 tạo file
	# load unitcode table 
	chars = []
	codes = []
	file = open("unicode.txt", encoding = "utf8") # để execute dc trên terminal fai có format đb là encoding
	unicode_table = file.read().split("\n")

	# split tiếp unicode_table làm list nhỏ chứa 2 elements gồm chữ và ký tự code
	#sau đó cho chữ và ký tự riêng ra vào 2 list chars, codes
	for code in unicode_table:
		x = code.split(" ")
		chars.append(x[0])
		codes.append(x[1])

	# Replace special characters in name and scores
	for i in range(len(codes)):
		name = name. replace(codes[i], chars[i])
		scores = scores.replace(codes[i], chars[i])
	# code trên: loop theo len chars or codes is ok, cz same size

	# with special char not in unicode use chr() function of python
	for i in range(len(name)):
		if name[i:i+2] == "&#":  # nums has index [i+2:i+5]
			name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:] # concatenate str
	for i in range(len(scores)):
		if scores[i:i+2] == "&#":		
			scores = scores[:i] + chr(int(scores[i+2:i+5])) +scores[i+6:] 



	#change to lower case
	name = name.title()
	scores = scores.lower()
	# split dob
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

	data =[sbd_str,name,str(dd),str(mm),str(yy)]

	# add scores to data
	for subject in ["toán", "ngữ văn", "khxn", "khtn", "lịch sử", "địa lý", "gdcd", "sinh học","vật lí", "hóa học", "tiếng anh"]:
		if subject in scores_list:
			data.append(str(float(scores_list[scores_list.index(subject)+1])))
		else:
			data.append("-1")



	# # open new file to check easily
	# file = open("test.txt", encoding = "utf8", mode ="a") # w=>a avoid overwrite
	# for i in range(len(data)):
	# 	file.write(data[i] + ",")
	# file.write("\n") # add \n into a file not data(each student)
	with open("clean_data.csv", "a", encoding ="utf8", newline="") as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)

# not : To make a file sbd_str that not exist execute try-except to copy all of it
# and then put it in if-countinue statement, because try functions took times
# use csv library ti make code smarter. if not newline="" then have emptyline