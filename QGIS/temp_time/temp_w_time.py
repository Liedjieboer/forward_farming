import numpy as np
import pandas as pd
#import dem data
data = pd.read_csv('QGIS/better_sheff_merge.csv')
#grab x,y and z values
x = data['x'].to_list()
y = data['y'].to_list()
z = data['z'].to_list()
#read shef data
df = pd.read_csv('clean_data/clean_sheff_data.csv')
#group by year
df_agg = df.groupby(by ='yyyy', as_index = False).agg({'avgtemp(degC)': 'mean',
                                                        'sun(hours)': 'mean',
                                                        'rain(mm)': 'sum',
                                                        'af(days)': 'sum',
                                                        'tmin(degC)': 'mean',
                                                        'tmax(degC)': 'mean'}
                                                       )
#cleaned df
df_new = df_agg[['yyyy','avgtemp(degC)']]
#add x,y and z columns for each year
df_new['x'] = [x]*94
df_new['y'] = [y]*94
df_new['z'] = [z]*94
#create a list of temp with alt calc applied to z
lst=[]
for idx, row in df_new.iterrows():
    lst.append(df_new.iloc[idx]["avgtemp(degC)"] - (0.98*np.array(row["z"])/100))
#add column for new list
df_new["temp_alt"] = lst
#convert to csv
df_new.tail(10).to_csv('QGIS/temp_time/temp_alt_time_data.csv',index=False)
