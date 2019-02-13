#Author: Jeremy Eudy

import json


def search(query, safeSearch=True, html=False, meanings=True):
    #Define url for API searches
    searchUrl = "https://api.duckduckgo.com/?q={}&format=json&atb=v1-1".format(query)
    safeSearch = '1' if safeSearch else '0'
    html = '0' if html else '1'
