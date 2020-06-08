from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 1
# -----------------------------------------------------------------------------------------
driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\0520\\4\\chromedriver.exe")
driver.get("https://www.walla.co.il/")
# driver.quit()