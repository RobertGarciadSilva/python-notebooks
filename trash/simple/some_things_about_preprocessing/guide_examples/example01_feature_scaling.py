
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler # applying standardScaler

data = pd.read_csv('./dataImported/dataTitanic/train.csv')

print(data.head(), end='\n\n')
print(data.isna().sum(), end='\n\n')
data['Age'].fillna(data['Age'].mean(), inplace=True)
dataAgeArray = data['Age'].values.reshape(-1,1)

# applying standard scaling

# applying z = (x - mean)/standard deviation about each row

feature_scaling = StandardScaler()

dataAgeScaled = feature_scaling.fit_transform(dataAgeArray)
print(dataAgeScaled)

dataFrameAgeScaled = pd.DataFrame(dataAgeScaled, columns=['age_escaled'])

print(dataFrameAgeScaled)





# reference
# https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9