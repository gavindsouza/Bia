# imports - standard imports
import os

# imports - third party imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# implementation functions:
# 1. auto form fill bot
# 2. link checker returns 0/1 bot

def formBot():
	# to be auto fill bot
	pass


def smartBot():
	# checks only 1 or 0
	pass


def url(site_url, webdriver_path):
	"""
	webdriver testing function
	opens the browser and site
	"""
	url = site_url
	browser = webdriver.Chrome(webdriver_path)
	browser.get(url)

	browser.close()


def __get_path_of_chrome_driver():
	# (finds)? and returns path of webdriver 
	# unnecessary: first checks a log file if path(s) exist else searches the whole drive for it
	chrome_path = os.abspath(r'\webdriver\chromedriver.exe')
	
	return chrome_path


def __tree(path, *args):
	# redundant function
	# from image_delete_from_movies.py
	# refactoring and linking needed
	# modify function to return webdriver path
    if path != '':
        path = path
    else:
        path = args
    try:
        for object in os.listdir(path):
            if os.path.isdir(path + '/' + object):
                tree(path + '/' + object)
            elif os.path.isfile(path + '/' + object):
                ext = object.split('.')[-1]
                if ext in image:
                    img.append('{0}/{1}'.format(path, object))

    except NotADirectoryError or FileNotFoundError or OSError:
        pass

