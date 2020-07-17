### driver code to create my datasets

import pandas as pd
from pytrends.request import TrendReq

search_period = '2019-06-02 2020-05-31' #search the past year

pytrends = TrendReq(hl='en-US', tz=420)
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness", "covid"] #list of keywords
kw_listextra = ["depression", "anxiety", "panic attack", "insomnia", "loneliness"]
kw_list_help = ["rehab", "meditation", "online therapy", "herbs", "online counseling"]

### Building the dataframe
df = pd.DataFrame({})
for id in kw_list:
    pytrends.build_payload([id], geo = 'US', timeframe = search_period)
    df[id] = pytrends.interest_over_time()[id]

df.to_excel('fname')