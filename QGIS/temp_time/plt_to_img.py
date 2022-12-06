import pandas as pd
import numpy as np
from darts import TimeSeries
import calendar
from darts.models import ExponentialSmoothing, TBATS, AutoARIMA, Theta, LinearRegressionModel
from darts.metrics import mae, mape
from darts.utils.statistics import extract_trend_and_seasonality
from darts.utils.utils import ModelMode
from darts.utils.utils import SeasonalityMode
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#getting the dem data
data = pd.read_csv('QGIS/better_sheff_merge.csv')

x = data['x'].to_list()
y = data['y'].to_list()
z = data['z'].to_list()

df = pd.read_csv('clean_data/clean_sheff_data.csv')

#creating a new table grouped by year
df_agg = df.groupby(by ='yyyy', as_index = False).agg({'avgtemp(degC)': 'mean',
                                                        'sun(hours)': 'mean',
                                                        'rain(mm)': 'sum',
                                                        'af(days)': 'sum',
                                                        'tmin(degC)': 'mean',
                                                        'tmax(degC)': 'mean'}
                                                       )

#using time series to predict future values
series_avg_ann = TimeSeries.from_dataframe(df_agg, "yyyy", "avgtemp(degC)")
train_avg_ann, val_avg_ann = series_avg_ann[:-1], series_avg_ann[-1:]
model_avg_ann = ExponentialSmoothing(trend=ModelMode.ADDITIVE, seasonal=SeasonalityMode.NONE)
model_avg_ann.fit(train_avg_ann)
prediction_avg_ann = model_avg_ann.predict(200, num_samples=1000)

#saving the predicted values
avg_list = []
for i in range(0,200):
    avg_list.append(prediction_avg_ann[i].mean()[0].first_value())

yyyy = list(range(2019,2219,1))

#new dataframe for year,temp,x,y,z data
df_new = pd.DataFrame()
df_new['yyyy'] = yyyy
df_new['avgtemp(degC)'] = avg_list
df_new['x'] = [x]*200
df_new['y'] = [y]*200
df_new['z'] = [z]*200

#creating data for temp with alt data
lst=[]
for idx, row in df_new.iterrows():
    lst.append(df_new.iloc[idx]["avgtemp(degC)"] - (0.98*np.array(row["z"])/100))

df_new["temp_alt"] = lst

#save as test img
for i in range(199,200):#len(df_new)
    ax = plt.gca()
    plt.imshow(df_new["temp_alt"].iloc[i].reshape(1723,1054))
    plt.clim(5.5,13.6)
    plt.grid(False)
    ax.xaxis.set_visible(False);
    ax.yaxis.set_visible(False);
    plt.savefig(f'QGIS/temp_time/imgs_for_time/{i+2019}.jpg',bbox_inches='tight',pad_inches=0.0)
