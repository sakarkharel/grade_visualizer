from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time 
from dotenv import load_dotenv
import os 

load_dotenv()

username = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://gap.westcliff.edu/")
driver.implicitly_wait(0.5)
username_box = driver.find_element(by = By.ID, value = "inputName" )
password_box = driver.find_element(by = By.ID, value = "inputPassword")
submit_button = driver.find_element(by = By.CSS_SELECTOR, value  = "button")
username_box.send_keys(username)
password_box.send_keys(password)
submit_button.click()
user_dropdown = driver.find_element(By.CLASS_NAME, "userbutton")
user_dropdown.click()
grades_link = driver.find_element(By.LINK_TEXT, "Grades")
grades_link.click()
time.sleep(5)  
course1_text = driver.find_element(By.ID, value = "grade-report-overview-10498_r0_c0")
course1_grades = driver.find_element(By.ID, value ="grade-report-overview-10498_r0_c1" )
course2_text = driver.find_element(By.ID, value = "grade-report-overview-10498_r1_c0")
course2_grades = driver.find_element(By.ID, value = "grade-report-overview-10498_r1_c1")
course3_text = driver.find_element(By.ID, value = "grade-report-overview-10498_r2_c0")
course3_grades = driver.find_element(By.ID, value = "grade-report-overview-10498_r2_c1")
course4_text = driver.find_element(By.ID, value = "grade-report-overview-10498_r3_c0")
course4_grades = driver.find_element(By.ID, value = "grade-report-overview-10498_r3_c1")
course5_text = driver.find_element(By.ID, value = "grade-report-overview-10498_r4_c0")
course5_grades = driver.find_element(By.ID, value = "grade-report-overview-10498_r4_c1")
print(course1_text.text)
print(course1_grades.text)
print(course2_text.text)
print(course2_grades.text)
print(course3_text.text)
print(course3_grades.text)
print(course4_text.text)
print(course4_grades.text)
print(course5_text.text)
print(course5_grades.text)



