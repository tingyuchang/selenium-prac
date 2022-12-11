from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# disable it if you want to open window  
display = Display(visible=0, size=(800,600))
display.start()

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

# WebDriver offers numbers of way to find elements
# see more in https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
# example 
"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
"""
elem = driver.find_element(By.NAME, "q")
# keyboard actions
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# final 
driver.close()