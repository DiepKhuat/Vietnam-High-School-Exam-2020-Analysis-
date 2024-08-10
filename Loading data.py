
import subprocess
start = 2000001
end = 2074719
file = open ("raw_data.txt","w")
for sbd in range (start,end):
	command = 'curl -L "https://diemthi.vnexpress.net/index/detail/sbd/0'+str(sbd)+'"/year/2020'
	result = subprocess.check_output(command)
	file.write(str(result) + '\n')  
# trên đã opne file h sẽ ghi all sbd vào file
 
