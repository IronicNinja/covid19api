import openpyxl
from datetime import date
import datetime

fname = 'covid_confirmed_usafacts.xlsx'
xfile = openpyxl.load_workbook(fname)

d0 = date(2020,1,22)
d1 = date.today()

sheet = xfile['sheet1']

states_list = {
'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0,
'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
'NH', 'NJ', 'NM', 'NY', 'NC', 'NC', 'OH',
'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
'WY'
}

c = 0
while sheet['D' + c] > 0:
  c += 1

xfile.save(fname)