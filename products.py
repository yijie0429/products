#讀取檔案
products = []
import os
if os.path.isfile('products.csv'):  #檢查檔案在不在
    with open ('products.csv', 'r',encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])
print(products)                                #印出橫的

#印出所有購買紀錄
for p in products:                             #印出直的:每讀取一次，印一次
    print(p[0], '的價格是', p[1])                      

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:           #打開一個檔案來寫入 #csv可用excel打開
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')      #四個都是字串，用字串合併

#我們所有需要寫入的程式碼，都要寫在with裡面，到第17行的時候，因為檔案已關閉，所以無法再寫入


