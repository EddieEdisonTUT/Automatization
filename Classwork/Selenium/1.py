from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sign_in_test(http, locator, login, password, submit):
    pass

# sign_in_test("https://github.com/login", By.NAME, 'login', 'password', 'commit')
# sign_in_test('http://opencart.qatestlab.net/index.php?route=account/login', )




def read_login():
    fin = open('/Users/student/Desktop/Automatization/Classwork/Selenium/login.txt')
    strs = fin.readlines()
    login_list = []
    for item in strs:
        login_list.append(item.split(' '))
    return login_list




login_list = read_login()
print(login_list)
for item in login_list:
    print(item)
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    login, password = item
    le_login = driver.find_element(By.NAME, 'login')
    le_pass = driver.find_element(By.NAME, 'password')
    le_login.send_keys(login)
    le_pass.send_keys(password)
    
    driver.close()
    # but = driver.find_element(By.NAME, 'commit')
    # but.click()



if "GitHub" in driver.title:
    print('OK')
else:
    print('Not OK')

