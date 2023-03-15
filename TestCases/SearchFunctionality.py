import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ProName = []
ServiceObj = Service("C:\\File D\\chromedriver.exe")
driver = webdriver.Chrome(service=ServiceObj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("c")
time.sleep(3)
Products = driver.find_elements(By.XPATH, "//div[@class='product']//h4[@class='product-name']")
for name in Products:
    ProName.append(name.text)
#print(ProName)
for cname in ProName:
    if "c" or "C" in cname:
        print(cname+" contains C letter")
    else:
        print(cname+" did not contains C letter")
VegetableName = driver.find_elements(By.CSS_SELECTOR, ".product-name")

for Vegitable in VegetableName:
    if Vegitable.text == "Cucumber - 1 Kg":
        driver.find_element(By.XPATH, "//a[@class='increment']").click()
        driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
        break

driver.close()
