from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

time_list = driver.find_elements(By.CSS_SELECTOR , ".shrubbery .menu time")
event_list = driver.find_elements(By.CSS_SELECTOR , ".shrubbery .menu a")

dic = {}

for i in range(0, len(time_list)):
    dic[i] = {
        "time" : time_list[i].get_attribute("datetime").split("T")[0],
        "name" : event_list[i].text
    }

print(dic)

# driver.close()
driver.quit()