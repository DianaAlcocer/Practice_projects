from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# Buscar el título
title_by_CSS = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")
title_by_TAGNAME = driver.find_element(By.TAG_NAME, "title")

# Imprimir resultado
print(f'Login form title: {title_by_CSS.text}')
print(f'Web title: {title_by_TAGNAME.get_attribute("innerText")}')

# Cerrar el navegador
driver.quit()
