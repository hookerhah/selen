#!/usr/bin/python
from selenium import webdriver
import selenium
import time
from time import sleep
import random
import os
from selenium.webdriver.chrome.options import Options
a = 0
def main():
	PROXY = "socks5://127.0.0.1:9050" # IP:PORT or HOST:PORT
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % PROXY)
	chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\ PATH')
	try:
		driver.set_page_load_timeout(10)
		driver.get("http://")
		print(a,'success')
		time.sleep(15)
		driver.quit()
	except:
		print(a,'not success')
		driver.quit()
while a < 100000:
	a += 1
	main()	
