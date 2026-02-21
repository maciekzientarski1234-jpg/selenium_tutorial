from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

# Stworzenie instancji klasy Chrome
# (to otworzy przeglądarkę)
driver = Chrome()
# Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")

# Maksymalizacja okna
driver.maximize_window()

# Znajdz element Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sleep(5)
# Kliknij w odnaleziony element
sign_in_a.click()

print(type(sign_in_a))
sleep(5)
driver.quit()