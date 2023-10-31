from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
options.add_argument("--incognito")


driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get('https://www.instagram.com/')
sleep(5)

# Localizar el elemento de entrada por su nombre
username_input = driver.find_element(
    # Hacer algo con el elemento
    By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
password_input = driver.find_element(
    # Hacer algo con el elemento
    By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
# Hacer algo con el elemento
login_btn = driver.find_element(
    By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')


# Rellenar el elemento de entrada
username_input.send_keys("")
password_input.send_keys("")
login_btn.click()
sleep(10)

driver.get('https://www.instagram.com/user')
sleep(5)


wait = WebDriverWait(driver, 10)
seguidores_btn = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//a[contains(text(),"seguidores")]')))
seguidores_btn.click()
sleep(15)

wait = WebDriverWait(driver, 10)
seguidor_btn = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//img[contains(@alt, "Foto del perfil de")]')))
seguidor_btn.click()
sleep(15)
