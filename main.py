from selenium.webdriver import Chrome
from time import sleep

# Stworzenie instancji klasy Chrome
# (to otworzy przeglądarkę)
driver = Chrome()
# Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")

# Maksymalizacja okna
driver.maximize_window()
sleep(5)
driver.quit()
