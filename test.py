from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

display = Display(visible=0, size=(800,600))
display.start()
driver = webdriver.Chrome()
driver.get("https://www.python.org")
print("tittle: ", driver.title)
assert "Python" in driver.title