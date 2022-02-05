from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver = webdriver.Chrome("C:\\Users\\dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
chromedriver.get("https:\\google.ca")
searchBtn = chromedriver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
searchBtn.send_keys("bedsheets")
searchBtn.submit()
linkWeb = chromedriver.find_element_by_xpath("//*[@id='tads']/div[1]/div/div/div[1]/a/div[1]")
linkWeb.click()
for link in searchBtn:

     print(searchBtn.get_attribute("href"))
   
searchBtn.click()
time.sleep(3.0)
chromedriver.back()