from automation.login import login_naukri
from automation.search_jobs import search_jobs
driver,wait = login_naukri()
search_jobs(driver,wait)


input("Press Enter to exit...")

driver.quit()