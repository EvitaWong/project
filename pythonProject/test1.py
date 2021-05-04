# coding = utf-8
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()

# browser.quit()

# driver = webdriver.Chrome()
# driver.maximize_window()
#
# first_url = "http://www.baidu.com"
# driver.get(first_url)
# print("access to %s" %{first_url})
#
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").cilck()
