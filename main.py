# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:43:32 2021

@author: AMEURBENNAOUI
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import time
from selenium.webdriver.common.keys import Keys
from fastapi.responses import JSONResponse
import os

import json
import pickle
import selenium.webdriver
import requests



def find_by_xpath(locator,driver):
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

        return element
def find_by_id(locator,driver):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, locator))
        )

        return element
def find_by_css(locator,driver):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , locator))
        )

        return element
def find_by_class(locator,driver):
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME , locator))
        )

        return element
def driver_mozilla(PROXY_HOST,PROXY_PORT):
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--hide-scrollbars')
    #options.add_argument('--disable-gpu')
    Username = "mabrouk"
    Password = "dragonball"
    myProxy="%s:%s" %(PROXY_HOST,PROXY_PORT)
    proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy, # set this value as desired
    'ftpProxy': myProxy,  # set this value as desired
    'sslProxy': myProxy,  # set this value as desired
    'noProxy': ''    ,     # set this value as desired
    'socksUsername': Username,
    'socksPassword': Password
    })
    ua = UserAgent()
    profile = webdriver.FirefoxProfile()
    
    profile.set_preference("general.useragent.override", ua.random)
    driver = webdriver.Firefox(proxy=proxy,firefox_profile=profile,firefox_options = options)
    return driver

def get_driver():
 
    try:
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == "chrome" or proc.name() == "chromedriver" or proc.name() == "Xvfb":
                proc.kill()    
    except:
        print('::::::::::::::::::::::::::::::::')

    with open("Config.json") as datafile:
            data = json.load(datafile)
    chrome_options = webdriver.ChromeOptions()
    if os.name=='nt' :   
        driver = webdriver.Chrome('chromedriver.exe',options=chrome_options) 
    else:
        driver = webdriver.Chrome('./chromedriver',options=chrome_options) 
    return driver



driver=get_driver()




pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))




cookies = pickle.load(open("cookies.pkl", "rb"))

s = requests.Session(cookies=cookies)

r = requests.session()
for c in cookies:
      r.cookies.update(c)





