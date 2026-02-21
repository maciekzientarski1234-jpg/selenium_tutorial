from selenium.webdriver import Chrome
from time import sleep

# stworzenie instalacji klasy Chrome
# to otworzy przegladarke
driver = Chrome()
# otwarcie strony
driver.get("https://www.kozminski.edu.pl/pl")
# maksymalizacja okna
driver.maximize_window()
sleep(5)
driver.quit()
