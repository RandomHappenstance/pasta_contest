from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from bs4 import BeautifulSoup as BS
import urllib

driver = webdriver.Firefox()

disabled = True

while disabled:
	url = urllib.urlopen('http://www.pastapass.com')
 	soup = BS(url)
 	a = soup.find('a', {'id':'ppp'})
 	print('disabled' in a['class'])
 	if 'disabled' not in a["class"]:
 		print('here')
 		disabled = False

driver.get('https://www.pastapass.com/')

elem = driver.find_element_by_id('ppp')
elem.click()

