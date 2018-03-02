#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:52:01 2018

@author: vivekkandathil
"""

import xml.etree.ElementTree as ET
from xmljson import parker
from json import dumps
import json
import requests
from json2html import *

#Get content from provided URL
xmlFile = requests.get('URL')

#Store binary data from url into xml file.
#'wb' (write binary) is required to write the page contents to a file in XML format.
with open('feed.xml', 'wb') as file:
    file.write(xmlFile.content)
    print('XML file created and written')

#parse xml file, get the root, and store in a string
tree = ET.parse('feed.xml')
root = tree.getroot()
xmlstr = ET.tostring(root, encoding='utf8', method='xml')

#convert to JSON using dumps method, in "parker" format
a = dumps(parker.data(ET.fromstring(xmlstr)), sort_keys=True, indent=4, separators=(',', ': '))

#write to JSON file
with open('File.JSON', 'w') as outfile:
    outfile.write((a))
    print("JSON File written") #Success message

#convert JSON to HTML
infoFromJson = json.loads(a)
htmlOutput = json2html.convert(json = infoFromJson)

#create and/or write JSON data to HTML file
with open('output.html', 'w') as file:
    file.write(htmlOutput)
    print('HTML file written')