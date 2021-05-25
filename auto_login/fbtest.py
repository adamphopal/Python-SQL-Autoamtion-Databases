from selenium import webdriver
from getpass import getpass
import time
from webdriver_manager.chrome import ChromeDriverManager


username = ''
password = getpass('What is the password for your facebook: ')

url = 'https://www.facebook.com/'

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

#time.sleep(2)

driver.find_element_by_id('loginbutton').click()
