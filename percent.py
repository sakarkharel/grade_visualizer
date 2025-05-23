from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time 
from dotenv import load_dotenv
import os 


def load_credentials():
    load_dotenv()
    username = os.getenv("MY_USERNAME")
    password = os.getenv("MY_PASSWORD")
    return username, password
    
    
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(0.5)
    return driver

def login(driver, username, password):
    driver.get("https://gap.westcliff.edu/")
    driver.find_element(By.ID, "inputName").send_keys(username)
    driver.find_element(By.ID, "inputPassword").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button").click()

def go_to_grades_page(driver):
    driver.find_element(By.CLASS_NAME, "userbutton").click()
    driver.find_element(By.LINK_TEXT, "Grades").click()
    time.sleep(5)
    
def extract_grades(driver):
    for i in range(5):
        course_text = driver.find_element(By.ID, f"grade-report-overview-10498_r{i}_c0")
        course_grade = driver.find_element(By.ID, f"grade-report-overview-10498_r{i}_c1")
        print(course_text.text)
        print(course_grade.text)  
        
def main():
    username, password = load_credentials()
    driver = setup_driver()
    
    try: 
        login(driver, username, password)
        go_to_grades_page(driver)
        extract_grades(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()







