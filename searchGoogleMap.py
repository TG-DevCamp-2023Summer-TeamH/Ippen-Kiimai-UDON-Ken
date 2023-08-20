# import library
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

# make csv data list
list_of_lists = []

with open("line_bot/templates/line_bot/udon-shop.csv", encoding="utf-8") as f:
    csv.reader(f)
    for row in csv.reader(f):
        list_of_lists.append(row)

# set webdriver path
wd = webdriver.Chrome(service=Service('C:/Users/soma_/Downloads/chromedriver_win32/chromedriver.exe'))

# access to Google Map Top
load_url = 'https://www.google.com/maps'
wd.get(load_url)
time.sleep(3)

# get every udon-shop details
row = -1
for list_data in list_of_lists:
    # count row
    row += 1
    
    # skip header
    if list_data[0] == "名前":
        continue
    
    # get search bar position
    search_box = wd.find_element(By.ID, "searchboxinput")
    search_box.send_keys(list_data[0])
    # get search button position
    search = wd.find_element(By.ID, "searchbox-searchbutton")
    search.send_keys(Keys.ENTER)
    
    # wait until push Enter key
    wait = input("Are You Selected It? [y/N]  ")
    
    # switch by output style
    if wait == "y" or wait == "Y":
        for _ in range(4 * 7 + 3):
            list_of_lists[row].append("")
    else:
        
        # review value
        review_point_text_place = wd.find_element(By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[2]")
        review_point_text = review_point_text_place.get_attribute("aria-label")
        review_point = ""
        for i in range(len(review_point_text)):
            if review_point_text[i] != " ":
                review_point += review_point_text[i]
            else:
                break
        review_point = float(review_point)
        review_items_place = wd.find_element(By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span")
        review_items_text = review_items_place.get_attribute("aria-label")
        review_items = ""
        for i in range(len(review_items_text)):
            if review_items_text[i] == ",":
                continue
            elif review_items_text[i] == " ":
                break
            review_items += review_items_text[i]
        
        # get share link
        share_button = wd.find_element(By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button")
        share_button.click()
        time.sleep(1)
        share_link = wd.find_element(By.CSS_SELECTOR, ".vrsrZe")
        googlemap_url = share_link.get_attribute("value")
        
        # close share spenit
        wd.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div[2]/button").click()
        
        # get open data
        opening = wd.find_element(By.CSS_SELECTOR, ".t39EBf.GUrTXd")
        opening_text = opening.get_attribute("aria-label")
        
        # edit open date
        days = ["日", "月", "火", "水", "木", "金", "土"]
        open_date = []
        box = ""
        for day in days:
            place = opening_text.find(day + "曜日、") + 4
            if opening_text[place].isdecimal():
                for i in range(13):
                    if opening_text[place + i].isdecimal():
                        box += opening_text[place + i]
                        if not opening_text[place + i + 1].isdecimal():
                            open_date.append(box)
                            box = ""
            elif opening_text[place] == "定":
                open_date.extend(["定休日", "", "", ""])
        
        # create shop detail array
        shop_detail = [googlemap_url, review_point, review_items]
        shop_detail.extend(open_date)
        
        # marge shop_detail to list_data
        list_of_lists[row].extend(shop_detail)
        
    # delete text from search bar
    for _ in range(len(list_data[0])):
        search_box.send_keys(Keys.BACKSPACE)
    
    # add to CSV file
    create_csv_path = r"c:\Users\soma_\Desktop\TwoGate_Dev_Camp\TwoGate_Dev_Camp\line_bot\templates\line_bot\udon-shop-detail.csv"
    f = open(create_csv_path, 'a', encoding="utf-8")
    print(list_of_lists[row])
    for i in range(len(list_of_lists[row])):
        if i == 10:
            continue
        if i + 1 != len(list_of_lists[row]):
            f.write(str(list_of_lists[row][i]) + ",")
        else:
            f.write(str(list_of_lists[row][i]) + "\n")
    f.close()