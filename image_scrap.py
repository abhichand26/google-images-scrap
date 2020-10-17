# -*- coding: utf-8 -*-

print("run imports...")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import urllib.request

def scrapClass(searchterm, no_images):
    #searchterm = 'asus rog laptop' # will also be the name of the folder
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    my_path = os.path.abspath(os.path.dirname(__file__))
    driverpath = os.path.join(my_path, "chromedriver.exe")
    browser = webdriver.Chrome(driverpath)
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0
    
    print("start scrolling to generate more images on the page...")
    # 500 time we scroll down by 10000 in order to generate more images on the website
    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")
    
    print("start scraping ...")
    #my_path = os.path.abspath(os.path.dirname(__file__))
    mainpath = os.path.join(my_path, "data/")
    folder = os.path.join(mainpath,searchterm)
    if not os.path.exists(folder):
        os.mkdir(folder)
    for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
        if(succounter == no_images):
            break
        counter = counter + 1
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)
        print("URL:", x.get_attribute('src'))
    
        img = x.get_attribute('src')
        new_filename = searchterm+"-"+str(counter)+".jpg"
    
        try:
            path = folder + "/"
            path += new_filename
            urllib.request.urlretrieve(img, path)
            succounter += 1
        except Exception as e:
            print(e)
    
    print(succounter, "pictures succesfully downloaded")
    browser.close()

# searchList contains the terms you want to scrap
searchList = ["asus rog laptop", "iphone 12", "oneplus 7t pro", "macbook 16 pro"]

for term in searchList:
    scrapClass(term, no_images=5)