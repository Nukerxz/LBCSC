#!/usr/bin/python3
# https://www.leboncoin.fr/collection/2226549042.htm                article au hasard pour faire les tests

import sys
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def mainmenu():
    print("-----Le Bon Coin Scam Check-----")
    print("Main Menu : -h for help")
    print("1 : Full scan")
    print("2 : Exit")
    rep = input("")
    if rep == "1":
        fullscan()
    if rep == "-h":
        print("usage : \ntype 1 for full scan")
        print("created by Nuker")
        print("ATTENTION : Ce script a pour but de vous aider dans vos recherches, en aucun cas il est vecteur de "
              "verite absolue et ne peut etre tenu pour "
              "responsable si vous manquez une bonne affaire ou tout autre desagrement.")
    if rep == "2":
        quit()
    if rep != "1" or rep != "-h" or rep != "2":
        print("pas compris")
        mainmenu()


def fullscan():
    url = input("paste your le bon coin url :")
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
        soup = BeautifulSoup(html_source_code, 'html.parser')
        for link in soup.find_all('img'):
            print(link.get('src'))
        title = soup.find("h1", {"data-qa-id": "adview_title"})
        name = soup.find("a", {"class": "_3k87M _3Hrjq _3Wx6b _2MFch _1hnil _35DXM _1-TTU _1GcfX _2DyF8 _3k00F"})
        desc = soup.find("p", {"class": "sc-iQNlJl bCyjVl"})
        print(title)
        print(name)
        print(desc)
        # print(soup.prettify())              pour print l'entierete du html
        browser.close()  # a mettre en fin de code


mainmenu()
