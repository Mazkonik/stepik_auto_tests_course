from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #Здесь в течении 12 сек проверяем цену на соответсвие 100$
    browser.find_element(By.ID, "book").click() 
    

    #button = browser.find_element(By.XPATH, "//button[@type='submit']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    #confirm = browser.switch_to.alert
    #confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
  
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #elements1 = browser.find_elements(By. CLASS_NAME, "form-control")
    #for element in elements1:
    #    element.send_keys("123")
       
    
    #option1 = browser.find_element(By.ID, "file")
    #current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'file.txt')         # добавляем к этому пути имя файла 
    #option1.send_keys(file_path)

   #button = browser.find_element_by_tag_name("button")
   #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   #button.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
