from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.keys import Keys
from time import sleep

co = webdriver.ChromeOptions()
co.add_argument("log-level=3")
co.add_argument("--headless")

def get_proxies():
    driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lesson_4\\chromedriver.exe")
    driver.get("https://free-proxy-list.net/")

    PROXIES = []
    proxies = driver.find_elements_by_css_selector("tr[role='row']")

    for p in proxies:

        # print(p)
        result = p.text.split(" ")

        if result[-1] == "no":
            PROXIES.append(result[0]+":"+result[1])

    driver.close()

    # print(len(PROXIES))

    return PROXIES

# 1
# -----------------------------------------------------------------------------------------
# options = Options()
# options.add_argument('--proxy-server=185.69.236.143:46454')
# driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lesson_4\\chromedriver.exe", options=options)
# driver.get("http://www.briza-club.co.il/")
#
# driver.find_element_by_name("name").send_keys("יוסי")
# driver.find_element_by_name("pass").send_keys("11111")
# driver.find_element_by_xpath('//*[@id="table6"]/tbody/tr[6]/td/input').click()


def proxy_driver(PROXIES, co=co):
    prox = Proxy()

    if PROXIES:
        pxy = PROXIES[-1]
    else:
        print("--- Proxies used up (%s)" % len(PROXIES))
        PROXIES = get_proxies()

    # prox.proxy_type = ProxyType.MANUAL
    # prox.http_proxy = pxy
    # prox.socks_proxy = pxy
    # prox.ssl_proxy = pxy
    #
    # capabilities = webdriver.DesiredCapabilities.CHROME
    # prox.add_to_capabilities(capabilities)
    #
    # driver = webdriver.Chrome(options=co, desired_capabilities=capabilities)

    print(pxy)
    return pxy


# ALL_PROXIES = get_proxies()
# print(ALL_PROXIES)
# ----------------------------------
# px = proxy_driver(ALL_PROXIES)


px = "45.70.106.34:8080"
options = Options()

# options.add_argument('--proxy-server=' + px)
driver = webdriver.Chrome(executable_path="C:\\Yossi\\DevOps\\Lesson_4\\chromedriver.exe", options=options)
driver.get("http://www.briza-club.co.il/")

driver.find_element_by_name("name").send_keys("יעל")
driver.find_element_by_name("pass").send_keys("02120601")
driver.find_element_by_xpath('//*[@id="table6"]/tbody/tr[6]/td/input').click()

driver.find_element_by_xpath('//*[@id="table97"]/tbody/tr[4]/td/input').click()


