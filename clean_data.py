import pandas as pd
import numpy as np

data = pd.read_csv('sheff_data.csv')
#access after 1929 as no sun data before this point
new_data = data[data['yyyy'] >= 1929]
#replace blank values with nan and fill na with previous rows value
new_data = new_data.replace('---',np.nan)
new_data = new_data.fillna(method='ffill')
#convert columns to right data types
new_data['tmax(degC)'] = new_data['tmax(degC)'].astype(float)
new_data['tmin(degC)'] = new_data['tmin(degC)'].astype(float)
new_data['af(days)'] = new_data['af(days)'].astype(float)
new_data['sun(hours)'] = new_data['sun(hours)'].astype(float)
#create avgtemp column
new_data['avgtemp(degC)'] = new_data[['tmax(degC)','tmin(degC)']].mean(axis=1)
#dataframe to csv
new_data.to_csv('clean_sheff_data.csv')
