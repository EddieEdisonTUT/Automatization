from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://flight.easemytrip.com/")

from_input = driver.find_element(By.ID, "FromSector_show")
from_input.send_keys("Delhi(DEL)")
time.sleep(2)

to_input = driver.find_element(By.ID, "Editbox13_show")
to_input.send_keys("Goa")
time.sleep(2)

departure_date_input = driver.find_element(By.ID, "ddate")
departure_date_input.send_keys("2023-09-01")
time.sleep(2)

search_button = driver.find_element(By.CLASS_NAME, "srchBtnSe")
search_button.click()

wait = WebDriverWait(driver, 50)
wait.until(EC.visibility_of_element_located((By.ID, "divFltMain")))

flight_elements = driver.find_elements(By.CLASS_NAME, "fltHpyRcomnFare")


number_of_flights = len(flight_elements)


print("Кількість знайдених авіарейсів з Delhi до Istanbul:", number_of_flights)


driver.quit()
