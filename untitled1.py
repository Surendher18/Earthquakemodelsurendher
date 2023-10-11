# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_OvLHQoOnKElvWIyFgn6_FgihrRNrXBH

```
**Earth quake prediction **
```
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import warnings
warnings.filterwarnings('ignore')

from google.colab import files


uploaded = files.upload()

df = pd.read_csv('all_month.csv')
df.head()

df.shape

plt.subplots(figsize=(15, 5))

plt.subplot(1, 2, 1)
sb.distplot(df['Depth'])

plt.subplot(1, 2, 2)
sb.boxplot(df['Depth'])

plt.show()

fig = plt.figure(figsize=(12,10))
plt.title("All affected areas")
m.plot(x, y, "o", markersize = 2, color = 'blue')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary()
m.drawcountries()
plt.show()