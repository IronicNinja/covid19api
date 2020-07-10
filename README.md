# covid19 API

This is the file from which I pull data from for my "Mental Health Post Covid19" Kernel, which can be found here: https://www.kaggle.com/ironicninja/mental-health-postcovid19. There are a couple of files here, each of which you may use to either replicate the results or create your own analysis.


# File Descriptions

The **convert.py** file is a file which converts a dataset from showing counties' covid numbers to showing states' covid numbers. The original dataset is here: https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/. Note that the code should convert everything up to your last Sunday, but for my purposes, the last week it converts is to July 5, 2020. Additionally, it starts converting the numbers on Janurary 26, 2020, which is the first Sunday after the dataset starts.

The **covid19scrape.py** file scrapes data from https://www.worldometers.info/coronavirus/ and inputs it into an excel sheet. Originally, I planned for this to be here to constantly update the values; however, the values to differ quite drastically from the usafacts dataset, and so I decided to cut off all searching after July 5, 2020. However, this code should still be fully functional, and values from 'state_covid19.xlsx' after July 7 have been updated with this code.

The **test.py** file takes the dictionary of 50 dataframes (each of which represent a state) and turn them separately into csv files. This was to prevent my code from getting rate limited, as 50 states times 6 operations for each state would quickly surpass the supposed 1400 requests rate limit. Each of the csv files is titled **data_** + [state abbreviation] + **.csv**, and so you are able to loop over state_abbreviation to get the dictionary of dataframes without having to send requests to google's server.


