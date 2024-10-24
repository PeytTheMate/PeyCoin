from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open browser and login
driver = webdriver.Chrome()  # or use a headless browser
driver.get('https://www.linkedin.com/login')

time.sleep(15)  # Wait for the page to loads

# Log in
email = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')
driver.find_element_by_css_selector('.login__form button')
email.send_keys('peytonkocher@gmail.com')
password.send_keys('@Pdawg2005')
driver.find_element_by_class_name('sign-in-form__submit-button').click()



# Search for people with your keywords
search_box = driver.find_element_by_xpath('//input[@placeholder="Search"]')
search_box.send_keys('software engineer' + Keys.RETURN)

time.sleep(15)

# Parse the search results
profiles = driver.find_elements_by_class_name('search-result__info')
for profile in profiles:
    profile_name = profile.find_element_by_tag_name('h3').text
    # Check for additional criteria
    if 'specific criteria' in profile_name:
        # Click connect button
        connect_button = profile.find_element_by_class_name('search-result__actions--primary')
        connect_button.click()
        time.sleep(2)
        
        # Send a message (after connecting)
        message_box = driver.find_element_by_tag_name('textarea')
        message_box.send_keys('Hi, I came across your profile and would love to connect!')
        send_button = driver.find_element_by_class_name('ml1')
        send_button.click()

# Quit browser
