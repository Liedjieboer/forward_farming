import pandas as pd
from darts import TimeSeries

# Read a pandas DataFrame
df = pd.read_csv("clean_sheff_data.csv", delimiter=",")

# Create a TimeSeries, specifying the time and value columns
series = TimeSeries.from_dataframe(df, "Month", "#Passengers")

# Set aside the last 36 months as a validation series
train, val = series[:-36], series[-36:]
