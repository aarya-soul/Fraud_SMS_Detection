# -*- coding: utf-8 -*-

print("Hi")

import sys, os

print sys.getdefaultencoding()

import re

def Find(string):
    #findall() has been used with all the valid connections for url in a string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

#Driver Code
val = raw_input("Paste the Text Message : \n")
print("Urls: ", Find(val))

from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq

for s in Find(val) :
    print(s)
    final_0 = s.replace('http://' , '')
    final_1 = final_0.replace('https://' , '')
    final = final_1.replace('www.' , '')
    web_name = final
    n_url = "https://www.urlvoid.com/scan/" + web_name + "/"
    
    #opens the connection and downloads html page from url
    uClient = uReq(n_url)
    page_html = uClient.read()  #It is used for ofloading the data nto a variable 

    # parses html into a soup data structure to transverse html as if it were a json data type
    page_soup = soup(page_html, "html.parser")
    uClient.close()
    
    containers = page_soup.tbody
    len(containers)

    contain = containers.findAll("tr")
    len(contain)

    data = contain[2].text
    data    # This data will be collected from the site regarding as the score of Website
    
    x = data[16]        # We only want 0 as the Answer so we locate it and store it into a value
    print(x)

    if x == "0" :
        print("You are visiting a Safe Website")
    else :
        print("You are visiting a Malicious Website")
