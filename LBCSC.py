#!/usr/bin/python3
# https://www.leboncoin.fr/collection/2226549042.htm

import sys
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

print('test')
if sys.argv[1] == "-h":
	print("usage : \npython3 LBCSC.py <your_leboncoin_url>")
	print("created by Nuker")

if sys.argv[1] != "-h":
	print("DISCLAIMER : This is not a '100%' accurate script, it has been made for helping to find if a seller is a scammer or not. Use it with caution.")
	url = str(sys.argv[1])

	HEADLESS_MODE = True
	JSON_FILE = "search-leboncoin.json"
	SEARCH_TERM = "Thinkpad"
	VERBOSE = True

	with sync_playwright() as p:
		browser = p.firefox.launch(headless=HEADLESS_MODE, slow_mo=70)
		page = browser.new_page()
		page.goto(url)
		accept_cookies_button = page.locator("button#didomi-notice-agree-button")
		accept_cookies_button.click()
		html_source_code = page.content()
		# print(html_source_code)
		soup = BeautifulSoup(html_source_code, 'html.parser')
		"""for link in soup.find_all('img'):
			print(link.get('src'))
		print(soup.prettify())"""
		for link in soup.find_all('name'):
			print(link)
		browser.close()       # a mettre en fin de code

dname = 'tg'
