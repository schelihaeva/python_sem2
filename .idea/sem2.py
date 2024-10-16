import pandas as pd


data = pd.read_csv('./kc_house_data.csv')
print(data.head())

data["sale_date"] =data['date'].astype("datetime64[ns]")
data = data.drop('date', axis=1)
print(data.head())

data['is_waterfront'] = data['waterfront'].astype(bool)
data = data.drop('waterfront', axis=1)
print(data.head())

data.info()

data.isna().sum()
data.isnull().sum()

data.describe()