#Author: Jeremy Eudy

import json
import requests
from urllib.parse import urlencode
import sys
import xml.etree.ElementTree as ET

def search(query, safeSearch=True, html=False, meanings=True):

    #Catch optional var changes
    safeSearch = '1' if safeSearch else '0'
    html = '0' if html else '1'

    #Define url params for API searches
    urlParams = {
            'q' : query, 
            'o': 'json', 
            'kp': safeSearch, 
            'no_redirect': '1', 
            'no_html' : html, 
            'd' : meanings
            }
    #Encode params into url format
    encoded = urlencode(urlParams)

    url = "https://api.duckduckgo.com/?"+encoded

    #get search response
    r = requests.get(url)

    #jsonify response
    if(urlParams['o'] == 'json'):
        j = json.loads(r.text)
        return j

    #or return xml
    elif(urlParams['o'] == 'x'):
        x = ET.fromstring(r.text)
        return x

def main():
    args = sys.argv[1:]
    args = ' '.join(args)
    result = search(args)
    return result

main()
