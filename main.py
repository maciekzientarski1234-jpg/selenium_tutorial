from itertools import dropwhile

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By


class Gender:
    MALE = 0
    FEMALE = 1

# Dane testowe
DATA_EMAIL = "kdhfsjdh@spam.la"
DATA_GENDER = Gender.MALE

# Stworzenie instancji klasy Chrome
# (to otworzy przeglądarkę)
driver = Chrome()
# Otwarcie strony
driver.get("https://www.kozminski.edu.pl/pl")
driver.implicitly_wait(10)
shadow_host = driver.find_element(By.ID, "usercentrics-root")

shadow_root = shadow_host.shadow_root
print(type(shadow_root))
btn = shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]')
btn.click()
sleep(4)