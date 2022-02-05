from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import pytest
import sys
import unittest

def youtube_search(search_query.num_result):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

 searchBtn = driver.find_element_by_name("search_query")
 searchBtn.send_Keys("punjabi songs")


num_result = driver.find_element(By.NAME ,"yt-lockup-video")
assertlen(searchBox) > = 5 , "Search results are less  than 5"
driver.close()



