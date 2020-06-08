from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lesson_4\\chromedriver.exe")
driver.get("file:///C:/Users/Yossi/PycharmProjects/calc/tip_calc/index.html")
driver.find_element_by_id("billamt").send_keys("110")
sleep(0.7)
tip = driver.find_element_by_xpath('//*[@id="serviceQual"]/option[5]')
sleep(0.7)
tip.click()

driver.find_element_by_id("peopleamt").send_keys("5")
sleep(0.7)
driver.find_element_by_id("musicQual").send_keys("1")
sleep(0.7)
driver.find_element_by_id("calculate").click()


#----------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def linked_in():
    driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lesson_4\\chromedriver.exe")
    driver.get("https://google.com")
    driver.find_element_by_name("q").send_keys("aviel buskila linkedin")
    driver.find_element_by_name("btnK").submit()
    driver.find_element_by_xpath("//a[starts-with(@href,\"https://www.linkedin\")]").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
    driver.find_element_by_name("session_key").send_keys("aviel33@gmail.com" + Keys.TAB + "123234" + Keys.ENTER)
    sleep(10)
# <a href="https://www.linkedin.com/avileb">Aviel Buskila LinkedIn </a>


linked_in()
