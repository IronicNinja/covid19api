from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from datetime import date
import math
import openpyxl
import pandas as pd

fname = 'https://www.governing.com/gov-data/census/state-minority-population-data-estimates.html'
req = Request(fname, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
page_soup = soup(webpage, "html.parser")

containers = page_soup.findAll("table")
container = containers[1]
A = container.findAll("tr")

tmp_list = [[], [], [], [], []]
for x in range(1, 52):
    if x == 9:
        continue
    B = A[x].findAll("td")
    for c in range(1, 6):
        s = str(B[c])
        s1 = s.replace('<td>', '')
        s2 = s1.replace('</td>', '')
        s3 = s2.replace('%', '')
        tmp_list[c-1].append(float(s3))

df = pd.read_excel('states_info.xlsx')
headers_list = ['hispanic', 'white', 'black', 'asian', 'american indian']

for pos in range(5):
    df[headers_list[pos]] = tmp_list[pos]

df.to_excel('states_info.xlsx')



