import time

from selenium.webdriver.common.by import By

from automation.login import login_naukri
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def search_jobs(driver=None,wait = None):
    searching_btn = wait.until(EC.element_to_be_clickable((By.ID,"ni-gnb-searchbar")))
    searching_btn.click()

    jobs_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter keyword / designation / companies']")
        )
    )

    jobs_input.send_keys('GenAI')

    exp_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Select experience']")
        )
    )
    exp_input.click()

    exp_dropdown_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='2 years']"))
        )
    exp_dropdown_input.click()

    # exp_input = Select(exp_input)
    # exp_input.select_by_visible_text('2 years')
    
    work_location = wait.until(
                EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter location']")
        )
    )
    work_location.send_keys("Mumbai")


    # Here ask user to verify the search quesry or he wants to filetes?
    # if not proceed 
    # else modify thne proceed

    applied_filters_search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ni-gnb-icn-search")))
    applied_filters_search.click()
