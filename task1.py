import pandas as pd
import numpy as np


hd = pd.read_csv("kc_house_data.csv")
stroki = hd.head()
avg = hd['price_per_sq_lot'] = hd['price'] / hd['sqft_lot']
hd["delta_renovared"] = np.where(hd["yr_renovated"]==0,hd["yr_renovated"], hd["yr_renovated"] - hd["yr_built"])
renv = hd["delta_renovared"]
year_ch = hd["date"].astype("datetime64[ns]").dt.year.astype("int64")
month_ch = hd["date"].astype("datetime64[ns]").dt.month.astype("int64")
new = hd.drop(columns=['date','zipcode', 'lat', 'long'], inplace=True)