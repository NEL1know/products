#記帳程式專案
#使用二維清單紀錄每次購買的商品及價格

import os # operating system
products = []

#檢查檔案在不在
if os.path.isfile('products.csv'): #只給檔名,即相對路徑.
	print('yeah 找到檔案了')
	#讀取檔案	
	with open('products.csv','r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #skip 到下一圈
			#strip()將空格跟分行脫掉
			#split(',')用逗號切割,切割完的結果是清單
			#s = line.strip().split(',')
			#name = s[0]
			#price = s[1]
			#原始有1個逗號,2個內容物,也可以如下寫法,分別儲存到2個變數中 
			name, price = line.strip().split(',')
			products.append([name,price]) 
	print(products)
else:
	print('找不到檔案')

#讓使用者輸入
while True:
	name =  input('請輸入商品名稱(離開請輸入q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	# 方式一
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	# 方式二
	# p = [name,price]
	# products.append(p)
	#簡易版寫法如下，不用創新空清單再append內容進清單
	products.append([name,price]) 
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
