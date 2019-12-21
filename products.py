# 讀去檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f: # 每一行
		if '商品,價格' in line:
			continue # 回到下一個 for 的判定
		name, price = line.strip().split(',') 
		# strip()去掉換行符號\n
		# 用','區分line裡面的資料
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # 'w' 寫入模式
# 使用utf-8編碼中文寫入才不會是亂碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # f.write 寫入
	# csv檔用逗點區隔 \n是換行
