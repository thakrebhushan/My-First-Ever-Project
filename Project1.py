from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome("exexutable_path=chromedriver.exe")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(1)

driver.find_element(By.NAME,'username').send_keys("Admin")   #  #Username
time.sleep(1)
driver.find_element(By.NAME,'password').send_keys("admin123")  # Password
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()   #lOGIN
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()  #Navigate to PIM
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()  #Add New Employee
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Bhushan")  # Add First Name
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys("Subhash")  # Add Middle Name
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("Thakre")   # Add Last Name
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()  # Save Details
time.sleep(2)



driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()  # Click Admin
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()  # Click on Add
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i').send_keys("Admin")  # Dropdown in User Role
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Bhushan Subhash Thakre")  # Employee Name
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').send_keys("Enabled")  # Status Enabled
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("Bhushan")  # Username, Bhushan
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Admin@123")  # Password is Admin@123
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Admin@123")  # Confirm Password is Admin@123
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()  # Save
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Bhushan")   # Username
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').send_keys("Admin")  # Select from Dropdown
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys("Bhushan Subhash Thakre")  # Employee Name
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i').send_keys("Enabled")  # Status Enabled
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()  # Search or Verify the User is Created
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'Logout').click()  # Logout

# Let's Re-login & Test
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Bhushan")  # Username
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("Admin@123")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()  # Login

