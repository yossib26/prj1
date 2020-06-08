from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lessson_4\\chromedriver.exe")
driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("walla" + Keys.ENTER)

# driver.get("file:///C:/Users/Yossi/PycharmProjects/calc/tip_calc/index.html")
#
# driver.find_element_by_id("billamt").send_keys("100")
#
# # tip =//*[@id="serviceQual"]
#
#
# # select = Select(driver.find_element_by_id('serviceQual'))
# # select.select_by_value('0.2')
#
# sleep(0.5)
# driver.find_element_by_id("serviceQual").send_keys("2")
#
# sleep(0.5)
# select2 = Select(driver.find_element_by_id('musicQual'))
# select2.select_by_value('0.1')
#
# sleep(0.5)
# driver.find_element_by_id("peopleamt").send_keys("4")




# driver.find_element_by_id("calculate").submit()


# driver.find_element_by_id("serviceQual").




# driver.get("http://www.google.com")

# driver.find_element_by_name("q").send_keys("walla")
# driver.refresh()


# driver.find_element_by_name("q").send_keys("walla")
# driver.find_element_by_id("tsf").submit()

# Xpath


