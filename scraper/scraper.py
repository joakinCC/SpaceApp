from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import time

#date stuff
from datetime import date, timedelta

import pandas as pd

import os
from os import listdir
from os.path import isfile,join

import glob, shutil # move file 


sdate = date(2018, 1, 1)   # start date
edate = date(2018, 12, 31)   # end date

delta = edate - sdate       # as timedelta

PATH_DOWNLOAD = r'C:\xxxx\xxxx\Downloads'

API_KEY = '07BE3DC0-B2CC-402B-9C4F-D5DE3B2CCFA4'
FORMAT = 'text/csv'
DISTANCE = '25'
ZIPCODE = '20002'

for i in range(delta.days + 1):
    DATE = sdate + timedelta(days=i)
    url = 'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=' + FORMAT + '&zipCode=' + ZIPCODE + '&date=' + str(DATE) + 'T00-0000&distance=' + DISTANCE + '&API_KEY=' + API_KEY 
    browser = webdriver.Chrome()
    browser.get(url)
    try:
        WebDriverWait(browser, 2)
        print("Página cargada!")
        time.sleep(2)
        browser.close()
    except TimeoutException:
        print("Tarda en cargar")

#moviendo todo a datos #tengo que moverlos de la carpeta descargas
for file in glob.glob(PATH_DOWNLOAD +'\*.csv'):
    shutil.move(file, 'datos')


# the next step is concatenate all csv files
mypath = ["datos"]

for anios in mypath:
    onlyfiles = [f for f in listdir(anios+"/") if isfile(join(anios+"/", f))]

    combined_csv = pd.concat( [ pd.read_csv(str(anios+"/")+f) for f in onlyfiles ], sort = False )
combined_csv.to_csv(anios+"/" +"big"+str(anios)+".csv", index=False )

exit()