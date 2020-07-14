from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from datetime import date
import math
import openpyxl

states_fullname = [
'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'missouri', 'mississippi',
'montana', 'nebraska', 'nevada', 'new-hampshire', 'new-jersey', 'new-mexico', 'new-york', 'north-carolina', 'north-dakota', 'ohio', 'oklahoma', 'oregon',
'pennsylvania', 'rhode-island', 'south-carolina', 'south-dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west-virginia',
'wisconsin', 'wyoming'
]

xfile = openpyxl.load_workbook('state_covid19.xlsx')
sheet = xfile['Sheet1']
diff = (date.today()-date(2020,7,7)).days + 168

### Converts a numerical value into an excel sheet's columns, so like "AF" or "EB"

code = ""
first_letter = math.floor((diff-1)/26)
code += chr(ord('@')+first_letter)
diff -= (first_letter*26)
code += chr(ord('@')+diff)

c = 2 # Starts at column 2
for states in states_fullname:
  fname = 'https://www.worldometers.info/coronavirus/usa/' + states + '/'
  req = Request(fname, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req)
  page_soup = soup(webpage, "html.parser")

  containers = page_soup.findAll("div", {"class": "maincounter-number"})
  container = containers[0]
  
  ### Replace spaces and commas
  num = container.span.text.replace(' ', '')
  num = num.replace(',', '')
  sheet[str(code) + str(c)].value = int(num)
  c += 1

xfile.save('state_covid19.xlsx')