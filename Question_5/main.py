"""
Write a program to download the data from the given API link and then extract the following data with
proper formatting

Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
Note - Write proper code comments wherever needed for the code understanding
"""

import pandas as pd
import json
import urllib.request
import bs4
import numpy as np

with urllib.request.urlopen('http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes') as f:
    dataa=json.loads(f.read().decode())
    
data_append=dict()
data_append['id']=[]
data_append['url']=[]
data_append['name']=[]
data_append['season']=[]
data_append['number']=[]
data_append['type']=[]
data_append['airdate']=[]
data_append['airtime']=[]
data_append['airstamp']=[]
data_append['runtime']=[]
data_append['rating']=[]
data_append['medium']=[]
data_append['original']=[]
data_append['summary']=[]
data_append['links']=[]
data_append['show']=[]

for i in dataa['_embedded']['episodes']:
    data_append['id'].append(i['id'])
    data_append['url'].append(i['url'])
    data_append['name'].append(i['name'])
    data_append['season'].append(i['season'])
    data_append['number'].append(i['number'])
    data_append['type'].append(i['type'])
    data_append['airdate'].append(i['airdate'])
    data_append['airtime'].append(i['airtime'])
    data_append['airstamp'].append(i['airstamp'])
    data_append['runtime'].append(i['runtime'])
    data_append['rating'].append(i['rating']['average'])
    data_append['medium'].append(i['image']['medium'])
    data_append['original'].append(i['image']['original'])
    data_append['summary'].append(bs4.BeautifulSoup(i['summary']).text)
    data_append['links'].append(i['_links']['self']['href'])
    data_append['show'].append(i['_links']['show']['href'])
    

d = pd.DataFrame(data_append)
d.to_csv("file.csv")