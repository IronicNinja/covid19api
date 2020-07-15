### https://dqydj.com/average-income-by-state-median-top-percentiles/

from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from datetime import date
import math
import openpyxl
import pandas as pd

fname = 'https://dqydj.com/average-income-by-state-median-top-percentiles/'
req = Request(fname, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
page_soup = soup(webpage, "html.parser")

containers = page_soup.findAll("table", {"class": "has-subtle-pale-green-background-color has-fixed-layout has-background"})
container = containers[0].findAll("tr")

tmp_list = []
for x in range(1, 52):
    if x == 8:
        continue
    tmp = container[x].findAll("td")
    s = str(tmp[1])
    s1 = s.replace('<td>', '')
    s2 = s1.replace('</td>', '')
    s3 = s2.replace('$', '')
    s4 = s3.replace(',', '')
    tmp_list.append(float(s4))

df = pd.read_excel('states_info.xlsx')
df['avg income'] = tmp_list
df.to_excel('states_info.xlsx')