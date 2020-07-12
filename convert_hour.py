from datetime import date
import pandas as pd
import datetime

diff = (date(2020, 7, 5) - date(2019, 7, 7)).days
df_str = pd.DataFrame({})

df = pd.read_excel('raw_hourly.xlsx')
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness"]

c = 0
while c < diff:
    type(c)
    tmp_dict = {'depression': 0, 'anxiety': 0, 'panic attack': 0, 'insomnia': 0, 'loneliness': 0}
    for hourX in range(24):
        for pos in range(len(kw_list)):
            tmp_dict[kw_list[pos]] += df.iloc[24*c + hourX][pos]
    s = pd.Series(tmp_dict)
    df_str[c] = (s/24)
    c += 1

df_str[c] = [df[keyword][len(df)-1] for keyword in kw_list]

df_save = df_str.T

df_save.to_excel('raw_daily.xlsx')