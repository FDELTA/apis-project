import hashlib
import datetime
from pprint import pprint as pp
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

def clean_header(x):
    x = x.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('?','')
    return x
def clean_nan(x):
    x = x.fillna('Unknown',inplace = True)
    return x
def fill_value(x,value):
    x = x.fillna(f'{value}', inplace=True)
    return x

def hash_params(alias):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = os.getenv('MARVEL_KEY')
    priv_key = os.getenv('MARVELP_KEY')
    
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    try:

        params = {'ts': timestamp, 'apikey': pub_key, 'hash': hashed_params,'name':alias}
        res = requests.get('https://gateway.marvel.com/v1/public/characters',params=params)
        results = res.json()
        data = results['data']['results']
        personaje = pd.DataFrame(data)
        comics = dict(personaje['comics'])
        comics2 = comics[0]['items']
        comics3 = []
        for x in comics2:
            comics3.append(x['name'])
        return print('Los 20 primeros comics por orden alfabetico:',comics3)
    except:
        print('No superhero match')
    
def statistical_info(x):
    data = pd.read_csv('output/marvel_characters.csv')
    m = data[x].mean()
    return print('The mean is:', m)