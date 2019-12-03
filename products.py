#記帳程式專案
#使用二維清單紀錄每次購買的商品及價格
products = []
while True:
	name =  input('請輸入商品名稱(離開請輸入q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
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

for p in products:
	print(p)