from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiAs8iS7uP4AhWdxDgGHfDjDaoQPAgI")
driver.get("https://www.amazon.in/")
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("apple iphone 13")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"//span[@xpath='1']").click()



