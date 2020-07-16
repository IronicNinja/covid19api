### converts covid data from daily to weekly

import pandas as pd
from datetime import date

fname = "covid_confirmed_usafacts.xlsx"
df = pd.read_excel(fname)

states_list = {
'AL': 0, 'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'FL': 0, 'GA': 0, 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0,
'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0,
'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0, 'OR': 0, 'PA': 0, 'RI': 0, 'SC': 0, 'SD': 0, 'TN': 0,
'TX': 0, 'UT': 0, 'VT': 0, 'VA': 0, 'WA': 0, 'WV': 0, 'WI': 0, 'WY': 0
}

covid_df = pd.DataFrame({})
diff = (date.today()-date(2020,1,22)).days + 4

c = 1
date = 4 # Starts from first sunday (after where the dataset starts, so 1/26/2020)
while date < diff:
  print(date)
  for c in range(1, len(df)):
    if df.iloc[c][2] == 'DC': #Don't include DC
      c += 1
      continue
    states_list[df.iloc[c][2]] += df.iloc[c][date]
    c += 1

  c = 1
  s = pd.Series(states_list)
  covid_df[date] = s
  for states in states_list:
    states_list[states] = 0
  date += 1

fname1 = "state_covid19.xlsx"
covid_df.to_excel(fname1)