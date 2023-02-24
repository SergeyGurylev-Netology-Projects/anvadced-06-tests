from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import YANDEX_LOGIN

driver = webdriver.Chrome()
driver.get("https://passport.yandex.ru/auth/")

elem = driver.find_element(By.ID, 'passp-field-login')
elem.send_keys('wrong_login')
elem.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CLASS_NAME, "Field-errorIcon"))
)

# elem.clear() -- почему-то для поля с логином не работатет
elem.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
elem.send_keys(YANDEX_LOGIN)
elem.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, "passp-field-passwd"))
)

elem = driver.find_element(By.ID, "passp-field-passwd")
elem.send_keys('wrong_password')
elem.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    # ec.presence_of_element_located((By.CLASS_NAME, "Field-errorIcon"))
    ec.presence_of_element_located((By.CLASS_NAME, "AuthPasswordForm-captcha"))
)

driver.close()