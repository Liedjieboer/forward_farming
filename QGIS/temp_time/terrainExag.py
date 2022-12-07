import pandas as pd
data = pd.read_csv('QGIS/better_sheff_merge.csv')

data['z'] = data['z'].apply(lambda x: 7*x)

data.to_csv('QGIS/temp_time/sheffield_exag.csv',index=False)
