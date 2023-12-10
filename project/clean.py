import pandas as pd
import requests
import re


def add_https(website):
    '''
    Function to add https prefix to website str
    input:
    website = string
    
    '''
    if not website.startswith('http'):
        return 'https://www.' + website
    else:
        return website