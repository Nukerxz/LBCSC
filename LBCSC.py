#!/usr/bin/python3

import webbrowser
import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def scan():
    url = input("Merci de coller votre lien LE BON COIN ici : ")
    print("Scan en cours de la page {}".format(url))
    HEADLESS_MODE = True

    with sync_playwright() as p:
        # permet de recuperer le code source de la page malgre datadome qui protege les requetes avec un cookie
        browser = p.firefox.launch(headless=HEADLESS_MODE, slow_mo=70)
        page = browser.new_page()
        page.goto(url)
        accept_cookies_button = page.locator("button#didomi-notice-agree-button")
        accept_cookies_button.click()
        html_source_code = page.content()
        soup = BeautifulSoup(html_source_code, 'html.parser')

        # recuperer toutes les images de la page
        images = []
        for image in soup.find_all('img'):
            images.append((image.get('src')))
        images = set(images)
        images = list(images)
        # print(*images, sep="\n") set a print le lien de chaque images
        co = 0
        for x in images:
            co += 1
        print("{} images ont été détectées, voulez-vous vérifier si ces images existent déjà en ligne ?".format(co))
        imagerep = input("y or n ? :")
        if imagerep == "y":
            for image in images:
                imagecheck(image)
        else:
            pass

        # le titre de l'annonce
        title = soup.find("h1", {"data-qa-id": "adview_title"})
        title = str(title)
        title = re.sub(r'<.+?>', '', title)
        print("Nom de l'article : ", title)

        # nom/pseudo de l'annonceur
        name = soup.find("a", {"class": "_3k87M _3Hrjq _3Wx6b _2MFch _1hnil _35DXM _1-TTU _1GcfX _2DyF8 _3k00F"})
        name = str(name)
        name = re.sub(r'<.+?>', '', name)
        print("Nom du vendeur : ", name)

        # description de l'article
        desc = soup.find("p", {"class": "sc-hXRMBi lgCcJw"})
        desc = str(desc)
        desc = re.sub(r'<.+?>', '', desc)
        print("Description de l'article : ", desc)
        descchecking = input("Voulez-vous vérifier si cette description existe autre part ? y or n : ")
        if descchecking == "y":
            desccheck(desc)

        # a mettre en fin de code
        browser.close()
        quit()


def mainmenu():
    print("-----Le Bon Coin Scam Check-----")
    print("1 : Full scan")
    print("2 : Help / Infos")
    print("3 : Exit")
    rep = input("")
    if rep == "1":
        scan()
    if rep == "2":
        print("created by Nuker")
        print("Ce script a pour but de vous aider dans vos recherches en automatisant certaines actions, merci "
              "de faire remonter toutes remarques, suggestions ou bugs directement sur le github disponible : "
              "https://github.com/Nukerxz/LBCSC")
        print("Utilisation :"
              "Tapez 1 puis coller l'url de l'article LE BON COIN que vous voulez scanner. "
              "L'url doit avoir ce format : https://www.leboncoin.fr/collection/0000000000.htm")

    if rep == "3":
        quit()
    else:
        mainmenu()


def imagecheck(imglink):
    webbrowser.open('http://www.google.com/searchbyimage?image_url={}'.format(imglink))


def desccheck(desc):
    webbrowser.open('https://www.google.com/search?q={}'.format(desc))


mainmenu()
