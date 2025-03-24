from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keep chrome open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#create webdriver, with options to keep it open
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page") #load a webpage

#Amazon product page price
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME, value="q")
# button = driver.find_element(By.ID, value="submit")

# By css selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

#copy xpath if it's hard to get an element
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# driver.close()    <-close tab
# driver.quit()     <-end the script

# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n]={
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
# print(events)

# articlecount = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(articlecount.text)


#click an element with .click()
#send text to an input with .send_keys()

#to press enter:
#   import Keys
#   .send_keys(Keys.ENTER)
# example for a search:
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

