import numpy as np
import pandas as pd
#dem data in csv format
data = pd.read_csv('~/code/Liedjieboer/forward_farming/QGIS/better_sheff_merge.csv')

#grabbing x,y and z data from csv
x = data['x'].to_list()
y = data['y'].to_list()
z = data['z'].to_list()

#how temp changes with altitude
# 0.98C per 100m

temp_change = [(15-((0.98*z[i])/100)) for i in range(len(z))]

#conver to np array for data use
temp_array = np.array(temp_change)

#convert to dataframe
coord = np.array([x,y,temp_array]).T
new_data = pd.DataFrame(coord)
#make it readable for qgis
#by making column names the first row of data
#i.e. x,y,z --> -184878.203,7089520.381,13.324200000000001
new_data.columns = new_data.iloc[0]
new_data = new_data[1:]

#turn into csv
new_data.to_csv('QGIS/temp_alt_data.csv',index=False)
