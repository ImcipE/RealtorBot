#function is passed a link, pulls out the propertly list HTML divs

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import Property
from create_property import create_property

browser = uc.Chrome()
browser.get("https://www.realtor.com/realestateandhomes-search/Akron_OH/type-multi-family-home/pnd-hide")
time.sleep(60)

#set target for pg_dn
target = browser.find_element(By.TAG_NAME,"body")

#grab HTML to compare:
soup_a = BeautifulSoup(browser.page_source, 'lxml')
properties = soup_a.find("section",{"data-testid":"property-list"})
check = "a"

#page down and compare source; quit when matched, meaning no new target HTML loaded on pgdn
while properties != check:
    target.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    check = properties
    soup_a = BeautifulSoup(browser.page_source, 'lxml')
    properties = soup_a.find("section",{"data-testid":"property-list"})

propertyList = properties.find_all("div",{"id":re.compile("^placeholder_property")})
browser.quit()

for prop in propertyList:
    create_property(prop)

Property.Property.writeInformation()