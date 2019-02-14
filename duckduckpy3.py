#Author: Jeremy Eudy

import json
import requests
from urllib.parse import urlencode

def search(query, safeSearch=True, html=False, meanings=True):

    #Catch optional var changes
    safeSearch = '1' if safeSearch else '0'
    html = '0' if html else '1'

    #Define url params for API searches
    urlParams = {
            'q' ; query, 
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
    j = json.loads(r.text)

    return Result(j)

class Result(object):

    def __init__(self, json):
        self.type = {'A' : 'answer', 'D' : 'disambiguation', 'C' : 'catagory',
                     'N' : 'name', 'E' : 'exclusive', '' : 'nothing'}.get(json.get('Type',''), '')

        self.json = json
        self.heading = json.get('Heading', '')
        self.results = [Result(elem) for elem
