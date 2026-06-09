from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.secrets import (
    NAUKRI_EMAIL,
    NAUKRI_PASSWORD
)

def login_naukri():

    driver = webdriver.Chrome()

    driver.get("https://www.naukri.com/")

    wait = WebDriverWait(driver, 20)

    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login_Layer")
        )
    )
    login_btn.click()

    email_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
        )
    )

    email_input.send_keys(NAUKRI_EMAIL)

    password_input = driver.find_element(
        By.XPATH,
        "//input[@type='password']"
    )

    password_input.send_keys(NAUKRI_PASSWORD)

    submit_btn = driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    )

    submit_btn.click()

    print("Logged in")

    return driver