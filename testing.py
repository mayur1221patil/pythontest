import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import HtmlTestRunner


class DemoblazeTest(unittest.TestCase):

    def setUp(self):
        webdriver_path = r'E:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
        service = Service(webdriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_demoblaze(self):
        driver = self.driver
        wait = self.wait

        # Open the website
        driver.get('https://demoblaze.com')

        # Sign up
        sign_up_button = wait.until(EC.element_to_be_clickable((By.ID, 'signin2')))
        sign_up_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, 'sign-username')))
        username_input = driver.find_element(By.ID, 'sign-username')
        password_input = driver.find_element(By.ID, 'sign-password')
        username = 'auto123'
        password = 'Auto123'
        username_input.send_keys(username)
        password_input.send_keys(password)
        sign_up_confirm_button = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
        sign_up_confirm_button.click()
        time.sleep(2)
        alert = Alert(driver)
        alert.accept()

        # Log in
        login_button = driver.find_element(By.ID, 'login2')
        login_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, 'loginusername')))
        time.sleep(1)
        login_username_input = driver.find_element(By.ID, 'loginusername')
        time.sleep(1)
        login_password_input = driver.find_element(By.ID, 'loginpassword')
        time.sleep(2)
        login_username_input.send_keys(username)
        login_password_input.send_keys(password)
        login_confirm_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_confirm_button.click()
        time.sleep(5)

        # Scroll down home page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Click next button on the home page
        next_button = driver.find_element(By.XPATH, '//*[@id="next2"]')
        next_button.click()
        time.sleep(2)

        # Add a product to the cart
        product = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')))
        product.click()
        time.sleep(2)

        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')))
        add_to_cart_button.click()
        time.sleep(2)

        # Handle alert
        try:
            alert = Alert(driver)
            alert.accept()  # Accept alert
        except:
            print("No alert found")

        # Go to cart
        cart_button = driver.find_element(By.ID, 'cartur')
        cart_button.click()
        time.sleep(2)

        # Log out
        logout_button = wait.until(EC.element_to_be_clickable((By.ID, 'logout2')))
        logout_button.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
