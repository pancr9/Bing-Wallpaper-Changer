#!Python 3
# Author: Rekhansh Panchal
# Tested on Python 3.5.2 with Windows 10
# Script to change daily wallpaper from bingwallpapers.
import urllib.request                                               # Library for web scrapping 
import ctypes                                                       # Library for calling DLL and shared libraries
import time                                                         # Library to get current time
import re                                                           # Library for regular expressions
dateToday = time.strftime("%Y%m%d")                                 # Get current date  
urlFetch = "http://bingwallpaper.com/" + dateToday + ".html"        # Create URL for the image


with urllib.request.urlopen(urlFetch) as response:                  # Obtain details from the URL
    html_doc = response.read()

from bs4 import BeautifulSoup                                       # Read details using BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')


imgTag =soup.find_all('img')[1]['src']                              # Getting src file for the wallpaper
filelink = "http:" + imgTag     
urllib.request.urlretrieve(filelink, "local-filename.jpg")          # Saving image locally

# Provide absolute path of saved image
path = "C:\\Users\\Rekhansh\\AppData\\Local\\Programs\\Python\\Python35-32\\local-filename.jpg"

SPI_SETDESKWALLPAPER = 20                                           # Setting wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
