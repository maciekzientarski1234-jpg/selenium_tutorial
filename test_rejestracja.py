from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from datatools import TestData
from datatools import Gender
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
        # 2. Wpisz e-mail
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        # 3. Kliknij "Create an account"
        self.driver.find_element(By.ID, "SubmitCreate").click()
        # 4. Kliknij swoją płeć
        if TestData.GENDER == Gender.FEMALE:
            # Kliknij Mrs
            self.driver.find_element(By.CSS_SELECTOR, 'label[for="id_gender2"]').click()
        else:
            # Kliknij Mr
            self.driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()

    def tearDown(self):
        self.driver.quit()