import pandas as pd
from pytrends.request import TrendReq
import pickle

search_period = 'today 12-m'

pytrends = TrendReq(hl='en-US', tz=420)
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness", "coronavirus"]

df = pd.DataFrame({})
for id in kw_list:
    pytrends.build_payload([id], geo='US', timeframe = search_period)
    df[id] = pytrends.interest_over_time()[id]

### populations link: https://www.statista.com/statistics/183497/population-in-the-federal-states-of-the-us/
### repub vs democrat (2018): https://news.gallup.com/poll/247025/democratic-states-exceed-republican-states-four-2018.aspx
states_list = {
    'AL': {'population': 4.9, 'repub': 52,'democrat': 35},
    'AK': {'population': 0.73, 'repub': 51,'democrat': 33},
    'AZ': {'population': 7.28, 'repub': 41,'democrat': 41},
    'AR': {'population': 3.02, 'repub': 48,'democrat': 35},
    'CA': {'population': 39.51, 'repub': 31,'democrat': 51},
    'CO': {'population': 5.76, 'repub': 40,'democrat': 47},
    'CT': {'population': 3.57, 'repub': 33,'democrat': 52},
    'DE': {'population': 0.97, 'repub': 35,'democrat': 48},
    'FL': {'population': 21.48, 'repub': 41,'democrat': 42},
    'GA': {'population': 10.62, 'repub': 42,'democrat': 43},
    'HI': {'population': 1.42, 'repub': 29,'democrat': 54},
    'ID': {'population': 1.79, 'repub': 50,'democrat': 34},
    'IL': {'population': 12.67, 'repub': 34,'democrat': 50},
    'IN': {'population': 6.73, 'repub': 46,'democrat': 38},
    'IA': {'population': 3.16, 'repub': 42,'democrat': 42},
    'KS': {'population': 2.91, 'repub': 47,'democrat': 36},
    'KY': {'population': 4.47, 'repub': 45,'democrat': 42},
    'LA': {'population': 4.65, 'repub': 45,'democrat': 37},
    'ME': {'population': 1.34, 'repub': 37,'democrat': 50},
    'MD': {'population': 6.05, 'repub': 31,'democrat': 54},
    'MA': {'population': 6.89, 'repub': 27,'democrat': 56},
    'MI': {'population': 9.99, 'repub': 39,'democrat': 45},
    'MN': {'population': 5.64, 'repub': 38,'democrat': 46},
    'MS': {'population': 2.98, 'repub': 48,'democrat': 36},
    'MO': {'population': 6.14, 'repub': 47,'democrat': 38},
    'MT': {'population': 1.07, 'repub': 46,'democrat': 39},
    'NE': {'population': 1.93, 'repub': 43,'democrat': 42},
    'NV': {'population': 3.08, 'repub': 38,'democrat': 45},
    'NH': {'population': 1.36, 'repub': 36,'democrat': 48},
    'NJ': {'population': 8.88, 'repub': 35,'democrat': 50},
    'NM': {'population': 2.1, 'repub': 38,'democrat': 48},
    'NY': {'population': 19.45, 'repub': 30,'democrat': 53},
    'NC': {'population': 10.49, 'repub': 42,'democrat': 41},
    'ND': {'population': 0.76, 'repub': 55,'democrat': 30},
    'OH': {'population': 11.69, 'repub': 45,'democrat': 41},
    'OK': {'population': 3.96, 'repub': 46,'democrat': 38},
    'OR': {'population': 4.22, 'repub': 38,'democrat': 47},
    'PA': {'population': 12.8, 'repub': 40,'democrat': 46},
    'RI': {'population': 1.06, 'repub': 36,'democrat': 43},
    'SC': {'population': 5.15, 'repub': 47,'democrat': 37},
    'SD': {'population': 0.88, 'repub': 51,'democrat': 40},
    'TN': {'population': 6.83, 'repub': 48,'democrat': 35},
    'TX': {'population': 29, 'repub': 42,'democrat': 39},
    'UT': {'population': 3.21, 'repub': 56,'democrat': 28},
    'VT': {'population': 0.62, 'repub': 30,'democrat': 55},
    'VA': {'population': 8.54, 'repub': 39,'democrat': 46},
    'WA': {'population': 7.61, 'repub': 35,'democrat': 50},
    'WV': {'population': 1.79, 'repub': 49,'democrat': 37},
    'WI': {'population': 5.82, 'repub': 43,'democrat': 43},
    'WY': {'population': 0.58, 'repub': 59,'democrat': 25}
}

state_df = {}

for state in states_list:
    df0 = pd.DataFrame({})
    for id in kw_list:
        pytrends.build_payload([id], geo='US' + '-' + state, timeframe = search_period)
        df0[id] = pytrends.interest_over_time()[id]
    state_df[state] = df0

pickle.dump(state_df, open("states_str.p", "wb"))