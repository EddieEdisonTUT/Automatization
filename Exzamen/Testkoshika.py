from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.get("https://rozetka.com.ua/")


search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("iPhone")
search_box.send_keys(Keys.RETURN)


time.sleep(2)  
product_link = driver.find_element(By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(1) .lazy_img_hover")
wait = WebDriverWait(driver, 10)
product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".catalog-grid__cell:nth-child(1) .goods-tile__title")))
product_link.click()
time.sleep(2)

add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".buy-button--tile")
wait = WebDriverWait(driver, 10)
add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".buy-button")))
add_to_cart_button.click()
time.sleep(2)

time.sleep(2) 
cart_count = driver.find_element(By.CSS_SELECTOR, ".cart-counter__input")
if cart_count.get_attribute("value") == "1":
    print("Товар успішно додано до кошика")
else:
    print("Помилка: товар не додано до кошика")

driver.quit()
