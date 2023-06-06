"""
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding.
"""

import pandas as pd
import json
import urllib.request
import bs4
import numpy as np

with urllib.request.urlopen("https://data.nasa.gov/resource/y77d-th95.json") as f:
    data1 = json.loads(f.read())
    
data1 = pd.DataFrame(data=data1)
data1.to_csv("meteorite.csv")