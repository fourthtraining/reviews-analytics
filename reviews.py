#留言分析程式
data = [] #建立空的清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) #把每一行加到data裡面
		count += 1 # count = count + 1
		if count % 1000 == 0:
			print(len(data))
		#print(line.strip()) #照順序印出並去除空格符號
		#print(len(data))
print(len(data)) #列出留言筆數

#print(data) #列出清單內所有留言
print(data[0]) #列出清單第一行
print('--------------')
print(data[1])