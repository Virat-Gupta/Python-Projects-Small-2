from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

EMAIL = "ENTER EMAIL HERE"
PASSWORD = "ENTER PASSWORD HERE"
PHONE = "ENTER PHONE HERE"

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get("https://www.linkedin.com/login/")

Email_Input = driver.find_element(By.XPATH, '//*[@id="username"]')
Password_Input = driver.find_element(By.XPATH, '//*[@id="password"]')

Email_Input.send_keys(EMAIL)
Password_Input.send_keys(PASSWORD)
Password_Input.send_keys(Keys.ENTER)
sleep(4)
driver.get(r"https://www.linkedin.com/jobs/search/?f_AL=true")
sleep(4)

def abort_application():
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    sleep(2)
    discard_button = driver.find_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]')
    discard_button.click()

all_job_listings = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
for job_listing in all_job_listings:
    if job_listing.get_attribute("data-occludable-job-id") == None :
        continue
    job_listing.click()
    try:
        apply_button =  driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        apply_button.click()
        sleep(2)

        phone_number_feild = driver.find_element(By.CSS_SELECTOR, "input.artdeco-text-input--input[required]")
        if phone_number_feild.text == "":
            phone_number_feild.send_keys(PHONE)
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button span")
        if submit_button.text == "Next":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            # Click Submit Button
            continue
    except NoSuchElementException:
        abort_application()
        print("No APPLICATION FOUND")
        continue

driver.quit()
