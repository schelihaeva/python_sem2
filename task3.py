import pandas as pd
import numpy as np

df = pd.read_csv("kc_house_data.csv")
avg = df.pivot_table(index='bedrooms', values='price', aggfunc='mean').sort_values(by='price')
price = df.groupby('condition').agg({'price': ['min', 'mean', 'max']})
print(price)
view_waterfront = df.pivot_table(index='waterfront', columns='view', values='id', aggfunc='count', fill_value=0)
bedrooms_floors = df.pivot_table(index='floors', columns='bedrooms', values='id', aggfunc='count', fill_value=0)
median_price = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)
