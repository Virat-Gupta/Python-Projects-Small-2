from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
timeout = time.time() + 5

def buyStuff() -> None:
    for item in store[::-1]:
        try:
            if item.get_attribute("class") != "grayed":
                item.click()
                return
        except:
            pass


while True:
    cookie.click()
    if timeout < time.time() :
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        buyStuff()
        timeout = time.time() + 5
        


