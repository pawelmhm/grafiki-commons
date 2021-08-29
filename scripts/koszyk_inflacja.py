#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv("../data/inflacja koszyk.csv")
data['2021'] = data['2021'].apply(lambda x: float(x.replace(",", ".")))
fig, ax = plt.subplots(figsize=(10,10))
plt.title('Koszyk inflacyjny 2021')
ax.pie(data['2021'], labels=data['WYSZCZEGÓLNIENIE'],  autopct='%1.1f%%', textprops=dict(fontname='sans serif'))
fig.show()

plt.savefig('../images/koszyk_inflacyjny_2021.png')