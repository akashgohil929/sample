from google.colab import files

uploaded = files.upload()

import pandas as pd
import numpy as np

df = pd.read_csv("")
print(df)
avg = df[""].mean()
print(avg)
df[""].fillna(avg, inplace=True)
print(df)
gender = df["gender"].mode()[0]
df[""].fillna(gender, inplace=True)

# bin
import math

data = np.sort()
bins_no = 3
bins = np.array_split(data, bins_no)
for i, bin_data in enumerate(bins):
    print(f"bin{i+1}:{bin_data}")

# minmax
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
df[""] = scaler.fit_transform(df[[""]])
