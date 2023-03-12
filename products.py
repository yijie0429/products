products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)                      #印出橫的
print(products[0][0])

for p in products:                   #印出直的:每讀取一次，印一次
    print(p[0], '的價格是', p[1])                      

    