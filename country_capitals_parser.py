import time
from selenium import webdriver
import requests
import sqlite3
xpaths=[] # create an empty list to store all pointers to data we're looking for
URL="https://www.thoughtco.com/capitals-of-every-independent-country-1434452" # assign target URL to the constant URL

connection=sqlite3.connect("results.db")
crsr = connection.cursor()

driver = webdriver.Chrome('/bin/chromedriver')  # initialize webdriver
driver.get(URL) # recieve target webpage, using selenium
time.sleep(2) # imitates real user :)


def getAllXpaths():           # function receives all pointers (xpath(-es)) to our target data and adds up to the xpaths[] list
    for li_i in range(1,197):   # hardcoded range determined with chrome developer tools
        xpath = "/html/body/main/article/div[4]/div[1]/div[7]/ol/li[{}]".format(li_i)
        xpaths.append(xpath)
    return xpaths

def getCapitalsList(data): # function recieves xpaths[] list and parse its data to create a final list [Country, Capital]
    country_capitals=[]    # create an empty list to store [Country, Capital]
    for data in range(len(xpaths)):     # iterate over the xpaths[] list to fetch its data
        capitals = driver.find_element_by_xpath(str(xpaths[data])).text    # get text content from each xpath in the list
        formatted_capitals = capitals.split(": ") # important to split not only by a semicolon, but additionally with a space after it, to get correct list items
        country_capitals.append(formatted_capitals)   # insert correctly formatted data to the country_capitals[] list
        global geo_dictionary
        geo_dictionary = dict(country_capitals) # creating a dictionary object which will be reused in Quiz Master

def capitalsTuple():
    cc_list = [(k, v) for k, v in geo_dictionary.items()]
    return cc_list

def addingToDB():
    crsr.execute('''CREATE TABLE IF NOT EXISTS Country_Capitals (Country TEXT,Capital TEXT);''')
    crsr.executemany('INSERT INTO Country_Capitals VALUES (?,?)', capitalsTuple())
    connection.commit()

def getDataFromDB():
    for rows in connection.execute('SELECT * FROM Country_Capitals'):
        fetched = [rows]
    print("List of Countries and its Capitals has been successfully added to the database!")

getAllXpaths()
getCapitalsList(xpaths)
capitalsTuple()
driver.quit()             # closing webdriver (browser)
addingToDB()
getDataFromDB()
