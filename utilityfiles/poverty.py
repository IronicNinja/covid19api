### https://worldpopulationreview.com/state-rankings/poverty-rate-by-state

import pandas as pd

df = pd.read_csv(r'C:\Users\evanz\Downloads\csvData.csv')

df1 = pd.read_excel('states_info.xlsx')
df1['poverty'] = df['poverty']
df1.to_excel('states_info.xlsx')