from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get(r"https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Test")
last_name.send_keys("Last")
email.send_keys("email@example.com")

submit_btn = driver.find_element(By.TAG_NAME, "button")
submit_btn.click()



# print(tot_articles.text)
