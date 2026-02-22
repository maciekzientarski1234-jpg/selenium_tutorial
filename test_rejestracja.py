from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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
        # Poczekam, aż będzie można kliknąć:
        # Metoda 1: Implicit wait
        # self.driver.implicitly_wait(10)
        # Metoda 2: Explicit wait
        if TestData.GENDER == Gender.FEMALE:
            # Kliknij Mrs
            gender_female = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="id_gender2"]')))
            gender_female.click()
        else:
            # Kliknij Mr
            gender_male = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[@for="id_gender1"]')))
            gender_male.click()
        # 5. Wpisz nazwisko
        self.driver.find_element(By.ID, "customer_firstname").send_keys(TestData.LAST_NAME)
        # 6. Sprawdź poprawność e-maila
        email_input = self.driver.find_element(By.ID, "email")
        email_actual = email_input.get_attribute("value")
        self.assertEqual(TestData.EMAIL, email_actual)
        # 7. Wpisz hasło
        self.driver.find_element(By.ID, "passwd").send_keys(TestData.VALID_PASSWORD)
        # 8. Wybierz datę urodzenia
        days = Select(self.driver.find_element(By.ID, "days"))
        days.select_by_value(TestData.BIRTH_DAY)
        months = Select(self.driver.find_element(By.ID, "months"))
        months.select_by_value(TestData.BIRTH_MONTH)
        years = Select(self.driver.find_element(By.ID, "years"))
        years.select_by_value(TestData.BIRTH_YEAR)
        # 9. Kliknij Register
        self.driver.find_element(By.ID, "submitAccount").click()

        sleep(2)

    def tearDown(self):
        self.driver.quit()