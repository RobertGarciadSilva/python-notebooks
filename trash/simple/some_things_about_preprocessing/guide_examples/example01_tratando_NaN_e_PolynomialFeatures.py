
import numpy as np
import pandas as pd

from sklearn.impute import MissingIndicator # Para tratar os valors nan, usado para guardar as ocorrências dos valores NaN.
from sklearn.impute import SimpleImputer # Para tratar os valores nan, substituindo eles por outro valor, por exemplo o valor da mediana.
from sklearn.preprocessing import PolynomialFeatures # Para transformações polinomiais


#Função para gerar simples random dataExported toy
def ger_random_data_Toy(num_rows=10,num_cols=4, min_value=0, max_value=100, size_Notnumber=0.1):
    """Gera random simple dataExported toys"""
    x = np.random.randint(min_value, max_value+1, num_rows*num_cols) #cria array com valores aleatorios baseado num argumentos fornecidos
    x = x.astype('float64') #transforma o array acima do tipo 'int' para o tipo 'float64'

    #Adiciona valores not a number no array acima, baseado no parametro passado para a porcentagem desses valores 'size_Notnumber'
    if(size_Notnumber > 0):
        quantNotNumber = int(size_Notnumber * (num_rows*num_cols))#numero de valores aleatorios
        for i in range(quantNotNumber):
            pos = np.random.randint(num_rows*num_cols)#sorteia posição para inserir valor aleatorio
            while(type(x[pos]) == 'nan'):#se a posição sorteada acima já contem um nan é sorteado outra posição até que ela não contenha nan.
                pos = np.randomint(num_rows * num_cols)
            x[pos] = np.NaN #coloca o valor nan no array

    x = x.reshape(num_rows, num_cols) #define o formato [num_rows, num_cols]
    return x


#Usando a função para gerar dados aleatorios
x = ger_random_data_Toy(num_rows=20, size_Notnumber=0.2)


#Criando dados aleatorios sem a função acima
#x = np.random.randint(0,100,40)
#x = np.append(x, [0,np.NaN, 9, np.NaN]).reshape(-1,4)


data = pd.DataFrame(x, columns=['feature1','feature2','feature3','featura4'])
data.to_csv(r'./dataExported/example01_tratando_NaN_e_PolynomialFeaturesBefore.csv', index=False, header=True) # salvando DataFrame dataExported em um arquivo
print(data, end='\n\n')

data.dropna(axis=0,thresh=3, inplace=True)
#deleta linhas com valores que não contém ao menos 3 valores nan, ou seja, linhas com 2,3 ou 4 valores nan são excluídas.
#axis: 0 para linha, 1 para coluna
#thresh: Quantidade de valores não nan que devem ter, as linhas ou colunas, para não serem excluídas.
#inplace: Executa sobre o próprio objeto, não retornando valor desse modo.

data.reset_index(inplace=True) # reseta os index
print(data, end='\n\n')

data.drop(['index'], axis=1, inplace=True) #exclui a coluna anterior que servia como index
print(data, end='\n\n')


# ------ Tratando valores nan.

#Conta o número de valores nan para cada coluna
countNaN = data.isna().sum()
print('Quantidade de nan por coluna:');print(countNaN, end='\n\n')

colNan = [] #usado para armazenar os nomes das colunas que apresentam valores NaN, esses nomes são criados adicionando '_bool_NaN' ao nome da coluna.
# essa lista é usada mais abaixo para nomear as colunas com valores NaN.

for i, val in zip(countNaN, countNaN.keys()): #armazena os novos nomes das colunas que apresentam valores nan.
    if(i > 0): # se a coluna apresenta valor NaN.
        colNan.append(val+'_bool_NaN')


indicator_nan = MissingIndicator(missing_values=np.NaN) #cria objeto MissingIndicator indicando que os valores NaN são valores do tipo np.NaN
indicator_nan = indicator_nan.fit_transform(data) #passa o DataFrame 'dataExported' como argumento para a função 'fit_transform' com retorno um array boolean indicando valores NaN.
dataFrame_indicatorNan = pd.DataFrame(indicator_nan, columns=colNan) #cria DataFrame com base no array acima

print(dataFrame_indicatorNan, end='\n\n')
# 'dataFrame_indicatorNan' guarda os valores NaN ocorrem, pode-se utilizar isso depois para verificar se essas indicações ajudam na construção de um melhor modelo.
# É interessante armazenar esses valores antes que tratemos, e assim perdemos, as ocorrências de NaN.


imputeNaN = SimpleImputer(missing_values=np.NaN, strategy='median')
data_imputed_NaN = imputeNaN.fit_transform(data)
data_imputed_NaN = pd.DataFrame(data_imputed_NaN, columns=data.columns.values)

print(data_imputed_NaN, end='\n\n') # Dados em que os valores NaN foram substituídos pela mediana de cada coluna.

# Acima foi usado a biblioteca sklearn para imputar, modificar os valores NaN do dataFrame pelas respectivas medianas,
# outra forma de fazer-se isso é utilizando o pandas.

data.fillna(data.median(), inplace=True)
print(data, end='\n\n')


# ---- polynomial features

#Aqui utilizamos o módulo 'PolynomialFeatures' do sklearn.preprocessing para
# a criação de relações, não lineares, entre as colunas númericas.

poly = PolynomialFeatures(degree=2, interaction_only=True)
#Aqui é criado o objeto PolynomialFeatures, em que:
# 'degree' representa o maior grau das relações e 'interaction_oly' = True representa que
# queremos relações apenas entre os valores das colunas e não entre uma coluna e ela mesma.
# os parâmetros colocados dessa forma nos dão, por exemplo, as seguintes relações:
# 1, feature1, feature2, feature3, feature4, feature1*feature2, feature1*feature3, feature1*feature4
# feature2*feature3, feature2*feature4, feature3*feature4
# Observe: Dois graus de liberdade para multiplicação e apenas relações entre as feature e não entre elas mesmas.
# Observe também que os primeiros 5 resultados são 1 e as próprias features, abaixo utilizamos um slice
# para retirar esses 4 primeiros valores e só pegarmos a partir do 5 valor.
# Observe a saída abaixo.

poly_features = poly.fit_transform(data)[:,5:] # aplicando fit.transform, pegando apenas a partir da quinta coluna de cada linha.

data_features_poly = pd.DataFrame(poly_features, columns=['feature1*feature2', 'feature1*feature3', 'feature1*feature4', \
                                                          'feature2*feature3', 'feature2*feature4', f'eature3*feature4'])

print(data_features_poly, end='\n\n')

# Abaixo realizamos a concatenação entre nossos dados originais (com modificação dos valores NaN ) e as novas colunas criadas.

print('\n\nDataFrame Final: '); print('\n')

data = pd.concat([data, dataFrame_indicatorNan,data_features_poly], axis=1)
data.to_csv(r'./dataExported/example01_tratando_NaN_e_PolynomialFeaturesAfter.csv', index=False, header=True) # Salvando dataExported final
print(data)

# Refereneces

# [1]https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9