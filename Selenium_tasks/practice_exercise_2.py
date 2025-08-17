import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
driver.implicitly_wait(5)

# Iniciar sesión
driver.find_element(By.ID, 'email').send_keys("Carol.015@gmail.com")
driver.find_element(By.ID, 'password').send_keys("qaengineer")
driver.find_element(By.CLASS_NAME, 'auth-form__button').click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Guardar el título de la tarjeta más reciente
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
print(f'Title before: {title_before}')

# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
titles = ['venecia', 'grecia', 'san francisco']
new_title = random.choice(titles)
driver.find_element(By.ID, 'place-name').send_keys(new_title)

# Insertar el enlace a la imagen en el campo Enlace
new_link = 'https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg'
driver.find_element(By.ID, 'place-link').send_keys(new_link)

# Guardar los datos
# driver.find_element(By.XPATH,".//button[@class='button popup__button']").click()
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/button[2]").click()

# Esperar a que aparezca el botón Eliminar
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/li[1]/button[@class="card__delete-button card__delete-button_visible"]')))

# Comprobar que la tarjeta tiene el título correcto
title_after = driver.find_element(By.XPATH, './/li[1]/div[2]/h2').text
print(f'Title after: {title_after}')
assert title_after == new_title

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(driver.find_elements(By.XPATH, ".//li[@class='places__item card']"))
print(cards_before)

# Eliminar la tarjeta
driver.find_element(By.XPATH, './/li[1]/button[@class="card__delete-button card__delete-button_visible"]').click()

# Esperar a que el título de la tarjeta más reciente sea igual a title_before
WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, './/li[1]/div[2]/h2'), title_before))

# Comprobar que ahora hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, ".//li[@class='places__item card']"))
print(cards_after)
assert cards_after == cards_before-1

driver.quit()
