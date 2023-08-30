from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get("https://www.selenium.dev/")


title = driver.title
print("Title of the page:", title)
time.sleep(5)

driver.quit()
