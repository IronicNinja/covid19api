import pandas as pd
from pytrends.request import TrendReq

search_period = '2020-01-26 2020-07-05' #search the past year

pytrends = TrendReq(hl='en-US', tz=420)
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness", "covid"] #list of keywords
kw_listextra = ["depression", "anxiety", "panic attack", "insomnia", "loneliness"]

### Building the dataframe
df = pd.DataFrame({})
for id in kw_listextra:
    pytrends.build_payload([id], geo='US', timeframe = search_period)
    df[id] = pytrends.interest_over_time()[id]

df.to_excel('covid_period.xlsx')