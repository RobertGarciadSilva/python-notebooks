
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import KBinsDiscretizer

data = pd.read_csv('./dataImported/dataTitanic/train.csv')
print(data.head())

print(data.columns.values, end='\n\n')
dataAge = data['Age']
print(dataAge.value_counts(dropna=True, normalize=True), end='\n\n')
print('Quantidade NaN em data[Age]: ', dataAge.isna().sum(), end='\n\n')
dataAge.fillna(dataAge.median(), inplace=True)
dataAgeValues = dataAge.values.reshape(-1,1)



# discretizando coluna 'Age'

age_discret = KBinsDiscretizer(n_bins=6, encode='ordinal')
age_discret_feat = age_discret.fit_transform(dataAgeValues)
#print(age_discret_feat.bin_edges_ , end='\n\n')
print(age_discret_feat)
print(age_discret.bin_edges_)
print(age_discret.n_bins_)

dataAgeDataFrame = pd.DataFrame(age_discret_feat, columns=['categorical_age'])
print(dataAgeDataFrame['categorical_age'].value_counts())

# Distribuição coluna 'Age'

fig, (ax, ax2) = plt.subplots(1,2, figsize=(12,5))
ax.hist(data['Age'], bins=20, edgecolor='black', color='r')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_title('Histograma coluna Age original')
ax.set_ylabel('Frequencia')
ax.set_xlabel('Age')
ax.grid(alpha=0.4)

ax2.hist(dataAgeDataFrame['categorical_age'], bins=6, edgecolor='black', color='r')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_title('Histograma coluna Age modificada')
ax2.set_ylabel('Frequencia')
ax2.set_xlabel('Age')
ax2.grid(alpha=0.4)



plt.show()
