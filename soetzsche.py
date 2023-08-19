import csv

list_of_lists = []

with open("test_data.csv", encoding="utf-8") as f:
  csv.reader(f)
  for row in csv.reader(f):
    list_of_lists.append(row)

s = 0
while s < len(list_of_lists):
  if (list_of_lists[s][4] == '') or (list_of_lists[s][4] == '1'):
    list_of_lists[s][4] = list_of_lists[s][3]
  print(list_of_lists[s][4] + " --> ", end='')
  for num in range(len(list_of_lists[s][4])):
    box = list_of_lists[s][4]
    if box[num] == 'r':
      list_of_lists[s][4] = ''
      break
    if box[num] == 'm':
      if box[num+1] == 'e':
        num += 17
      list_of_lists[s][4] = ''
      if box[num+1] == " ":
        break
      for im in range(12):
        if num+im == len(box):
          break
        list_of_lists[s][4] += box[num+im]
        if list_of_lists[s][4] == 'm52000181910':
          list_of_lists[s][4] = ''
        elif list_of_lists[s][4] == 'm70588573678':
          list_of_lists[s][4] = ''
      break
    if num == len(list_of_lists[s][4]) - 1:
      list_of_lists[s][4] = ''
  print(list_of_lists[s][4])
  s+=1
print()
print()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

wd = webdriver.Chrome(service=Service('C:/Users/soma_/Downloads/chromedriver_win32/chromedriver.exe'))

count = -1
sp_count = 0
url_list = []
sold_list = []
mistake = 0

for s in range(len(list_of_lists)):
  if list_of_lists[s][4] != '':
    stock = "売り切れ及び削除済み商品です。"
    load_url = "https://jp.mercari.com/item/" + list_of_lists[s][4]
    url_list.append(load_url)
    count += 1
    if count % 1 == 0:
      sp_count += 1
      print()
      print('-------------------------------------------------------')
      print(sp_count)
      print()
    print(load_url)
    number_of_time = 1
    for triple_check in range(3):
      wd.get(load_url)
      time.sleep(4)
      hc = wd.page_source
      if "購入手続きへ" in hc:
        stock = "在庫あり商品です。"
      print(number_of_time, "回目 在庫確認済みです。", stock)
      if (stock == "在庫あり商品です。"):
        if (number_of_time == 2):
          print("【 1 回目 誤検出を確認 】")
          mistake += 1
        elif (number_of_time == 3):
          print("【 1,2 回目 誤検出を確認 】")
          mistake += 2
        break
      number_of_time += 1
    if (stock == "売り切れ及び削除済み商品です。"):
      sold_list.append(load_url)
      print("リストに追加しました。")
wd.quit()

sold_count = 0
print()
print('-------------------------------------------------------')
print('-------------------------------------------------------')
print()
print('本日の在庫チェックが終了しました。')
print("本日の売り切れ及び削除済み商品を下に表示します。")
print()
for out in range(0, len(sold_list)):
  print(sold_list[out])
  sold_count += 1
print()
print("total:", sold_count)
print("mistake:", mistake)
print()
print('-------------------------------------------------------')