
import numpy as np
import pandas as pd

from sklearn.preprocessing import OrdinalEncoder # Encoder ordinal feature
from sklearn.preprocessing import OneHotEncoder # Encoder nominal feature

#Criando dataExported toy

ndataArray = np.array(['M','O-','medium',
                       'M','O-','high',
                       'F','O+', 'high',
                       'F','AB','low',
                       'F','B+', np.NaN]).reshape(5,3)

data = pd.DataFrame(ndataArray, columns=['sex','blood_type','edu_level'])
print(data, end='\n\n')
data.to_csv(r'./dataExported/example01_data_categorical_featuresInicio.csv', index=False, header=True) # salvando os dados em um arquivo.

# Ordinal feature (edu_level)

data_t = data.copy()

encoder = OrdinalEncoder()

data_t['edu_level'] = encoder.fit_transform(data_t['edu_level'].values.reshape(-1,1))
print(data_t)
# Repare que pelo modo com que é feito o OrdinalEncoder, o valor NaN foi
# substituído por outro valor, no teste realizado aqui '3' e
# os novos valores da coluna não respeitam a ordem 'low', 'medium', 'high',
# uma maneira melhora para se fazer isso é utilizando o próprio pandas.


cat_edu_level = pd.Categorical(data['edu_level'],
                               categories=['missing', 'low',
                                           'medium','high'],
                               ordered=True)
print(cat_edu_level, end='\n\n') # Observe a saída como um array do tipo Catecorical contendo a ordem dos valores passados

cat_edu_level =  cat_edu_level.fillna('missing') # substituíndo o valor NaN da coluna pela categoria 'missing' ( Observe que o tratamento feito aqui para o valor NaN é feito de forma arbitrária apenas para continuar o exemplo )
print(cat_edu_level, end='\n\n')

labels, unique = pd.factorize(cat_edu_level, sort=True) # Para mais detalhes sobre a função 'factorize' consulte a referencia abaixo sobre.
print('labels: ', labels)
print('unique: ', unique) # Observe que passando sort como True unique é retornado ordenamente, sendo o primeiro valor 0, o segundo 1 e assim por diante.

data['edu_level'] = labels
print(data, end='\n\n') #Observe agora que a categorização por inteiros respeita a ordenação colocada acima e 'missing' (NaN) é colocado como categoria 0 (pela ordenação colocada acima).


# nominal feature (sex, blood_type)

oneHot = OneHotEncoder(dtype=np.int)
nominals_features = oneHot.fit_transform(data[['sex', 'blood_type']])

nominals_features = nominals_features.toarray()
print(nominals_features)
# observe que a saída em 'nominals_features' é uma matrix sparsa, logo convertemos ela para um array usando .toarray()
# Isso pode ser feito também colocando um parâmetro em OneHotEncoder(sparse=False)

# Para vermos como OneHot realizou a ordem da categorização podemos usar
print(oneHot.categories_)

#colocando em um DataFrame temos
nominals_features = pd.DataFrame(nominals_features, columns=['F','M','AB','B+','O+','O-']) # Mesma ordem oneHot_categories_
print(nominals_features, end='\n\n')

# abaixo podemos comparar o mesmo conjunto de dados inicial só que melhor tratado para os algoritmos de ML

newData = pd.concat([nominals_features, data['edu_level']], axis=1)
print(newData)
newData.to_csv(r'./dataExported/example01_data_categorical_features_DepoisDeTratado.csv', index=False, header=True)

# References

# https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.factorize.html
