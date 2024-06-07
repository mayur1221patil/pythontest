from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
webdriver_path = r'E:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
username = 'your_username'
password = 'your_password'

# Create a Service object
service = Service(webdriver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)

# Define a function to log the result
def log_result(step, result):
    with open('test_execution_report.txt', 'a') as report:
        report.write(f"{step}: {result}\n")

try:
    # Open the Demoblaze website
    driver.get('https://demoblaze.com')
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, 'login2').click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'loginusername')))
    driver.find_element(By.ID, 'loginusername').send_keys(username)
    time.sleep(2)
    driver.find_element(By.ID, 'loginpassword').send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
    log_result('Login', 'Success')
    time.sleep(1)
    # Scroll down the home page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the scrolling to complete
    log_result('Scroll down home page', 'Success')

    # Click on next button of home page
    next_button = driver.find_element(By.CLASS_NAME, 'page-link')
    next_button.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Add the first product of the page into the cart
    first_product_add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
    first_product_add_to_cart_button.click()
    time.sleep(2)
    # Go to cart
    driver.find_element(By.ID, 'cartur').click()
    time.sleep(2)  # Wait for the cart page to load
    log_result('Go to cart', 'Success')
    time.sleep(2)
    # Logout
    driver.find_element(By.ID, 'logout2').click()
    log_result('Logout', 'Success')

except Exception as e:
    log_result('Test execution', f'Failed due to {e}')
finally:
    driver.quit()

# Displaying the test execution report
with open('test_execution_report.txt', 'r') as report:
    print(report.read())
