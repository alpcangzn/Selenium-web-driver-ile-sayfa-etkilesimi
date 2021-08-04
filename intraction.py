from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Drivers\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

articleCountalp = driver.find_elements_by_css_selector(".main-top-articleCount a")[1]
#sayfalar = driver.find_element_by_link_text("Sayfalar")
#articleCountalp.click()
#time.sleep(3)
#sayfalar.click()

searchInput = driver.find_element_by_name("search")
searchInput.send_keys("Fenerbahce")
searchInput.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()