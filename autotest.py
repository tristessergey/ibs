from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.google.com/ncr")
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element.send_keys('selenide')
element.send_keys(Keys.ENTER)
result = driver.find_element_by_tag_name('h3')
pictures = driver.find_element_by_link_text('Картинки')
pictures.click()
sleep(3)
