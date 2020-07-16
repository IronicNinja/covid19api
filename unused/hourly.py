import pandas as pd
from pytrends.request import TrendReq

search_period = '2019-07-07 2020-07-05' #search the past year

pytrends = TrendReq(hl='en-US', tz=420)
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness", "covid"] #list of keywords
kw_list2 = ["panic attack", "insomnia", "loneliness", "covid"]
kw_list3 = ["insomnia", "loneliness", "covid"]
kw_list4 = ["loneliness", "covid"]
kw_list5 = ["covid"]

### Building the dataframe
df = pd.DataFrame({})
for id in kw_list5:
    print(id)
    df[id] = pytrends.get_historical_interest([id], year_start=2019, month_start=7, day_start=7, year_end=2020, month_end=7, day_end=5, sleep = 3)[id]

df.to_excel('raw_hourly4.xlsx')