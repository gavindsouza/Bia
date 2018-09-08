from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import combinations_with_replacement, combinations



def url(site_url, webdriver_path):
	url = site_url #r"https://115.248.171.105:100/"
	browser = webdriver.Chrome(webdriver_path) #r"C:\Users\Gavin\Desktop\Code\Python\other\chromedriver.exe"
	browser.get(url)



	browser.close()



def generate_keys(suggested):
	"""
	Inputs suggested keywords to generate likely list of passwords
	"""
	pass_list = []

	"""
	for r in range(8, 16):
		pass_list += 
	"""
	
	for r in range(11,12):
		pass_list = [''.join(x) for x in combinations(''.join(['180197','gavin','1997']), r)]


	return pass_list
