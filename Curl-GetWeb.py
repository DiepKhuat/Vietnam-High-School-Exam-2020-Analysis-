'''
step 1: trên terminal dùng lệnh curl để gửi lệnh lấy thông tin trên web về terminal(1 thí sinh)
C:\Users\USER>curl - F "sobaodanh=02074718"diemthi.hcm.edu.vn/Home/Show
sobaodanh=02074718 và /Home/Show thì vào web click right, select View page source xem form là hiểu
step2: lưu data lấy trên terminal về và execute trên python bằng code sau:
import subprocess	__init__
result = subprocess.check_output('curl - F "sobaodanh=02074718"diemthi.hcm.edu.vn/Home/Show')
print (result)
**lý do chạy = code vì có thể loop dc cho nh người
step3: tạo file text gồm all các thí sinh
vào FileIO.py get details
file = open ("raw_data.txt", "w")
file.write(str(result))
step 4: dùng for loop
concatenate là nối str
'''
import subprocess
start = 2000001
end = 2074719
file = open ("raw_data.txt","w")
for sbd in range (start,end):
	command = 'curl - F "sobaodanh=0'+ str(sbd) +'"diemthi.hcm.edu.vn/Home/Show'
# 'curl - F "sobaodanh=02074718"diemthi.hcm.edu.vn/Home/Show' đây là result của 1ng
# loop cho các số lặp từ start-end thì chỗ lặp là 7# còn lại nên tách str sobaodanh=0 
	result = subprocess.check_output(command)
	file.write(str(result) + '\n')  
# trên đã opne file h sẽ ghi all sbd vào file