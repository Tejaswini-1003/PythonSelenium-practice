from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.fullscreen_window()
time.sleep(6)
driver.find_element(By.XPATH,"//a[@id='booking_engine_hotels']").click()
time.sleep(6)
# driver.find_element(By.ID, "lname")
print(driver.title)
