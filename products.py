import os
#讀取檔案
def read_file(filename):
    products = []
    with open (filename, 'r',encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)    
    return products                            #印出橫的

#印出所有購買紀錄
def print_products(products):
    for p in products:                             #印出直的:每讀取一次，印一次
        print(p[0], '的價格是', p[1])                      

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:           #打開一個檔案來寫入 #csv可用excel打開
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')      #四個都是字串，用字串合併

#我們所有需要寫入的程式碼，都要寫在with裡面，到第17行的時候，因為檔案已關閉，所以無法再寫入

#每一個def都是封閉的功能，因此必須要將第一個清單拉出來，導入到第二個def，更新後再拉出來到第三個def寫入
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):                   #檢查檔案在不在
        products =  read_file(filename)      #read_file('products.csv')讀取完後的結果為清單，存到products，所以現在products為清單
    else:
        products('找不到檔案')

    products =  user_input(products)           #把41行讀取的products清單丟到def user_input(products)，這樣它才會知道這裡的products是清單，新增完清單後再存回products
    print_products(products)                   #再把products清單丟進去，讓for去讀取清單印出來
    write_file('products.csv', products)

main()

