# import library
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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
for list_data in list_of_lists:
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
        for _ in range(len(list_data[0])):
            search_box.send_keys(Keys.BACKSPACE)
        continue
    
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
    
    # edit opening date
    
    
    # output to command line
    print()
    print(list_data[0])
    print("☆", review_point, review_items)
    print(googlemap_url)
    print(opening_text)
    print()
    
    # delete text from search bar
    for _ in range(len(list_data[0])):
        search_box.send_keys(Keys.BACKSPACE)