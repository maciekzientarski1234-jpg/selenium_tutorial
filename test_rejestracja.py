from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unittest



class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")
        # 2. Użytkownik niezalogowany
        # (opcjonalnie) można sprawdzić

    def test_no_name_in_registration_form(self):
        # KROKI
        # 1. Klinkij "Sign in"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        # Czekam (usunę po napisaniu testu)
        sleep(2)

    def tearDown(self):
        self.driver.quit()