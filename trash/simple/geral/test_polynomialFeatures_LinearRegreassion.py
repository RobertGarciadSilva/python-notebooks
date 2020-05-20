

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def make_data(size=100, desv=0.6):
    rns = np.random.RandomState(42)
    x = rns.rand(size)
    y = -1/(x + 0.1) # função y = -1/(x + 0.1)
    if(desv > 0):
        y += rns.randn(size)*desv

    return x, y

X, y = make_data()


# --- aplicando LinearRegression

X2 = np.linspace(0,1,500) # intervalo escolhiod devido ao uso de rand() que varia entre 0 e 1

model_linear = LinearRegression()
y_model = model_linear.fit(X[:, np.newaxis], y).predict(X2[:, np.newaxis])
model_linear




# ---- aplicando PolynomialFeatures e depois LinearRegression

pol = PolynomialFeatures(degree=3)

X_polyFeat = pol.fit_transform(X[:, np.newaxis])
X2_polyFeat = pol.fit_transform(X2[:, np.newaxis])

#print(pol.get_feature_names()) # nome das colunas obtido ao plicar a transformação com PolynomialFeatures
print(pol.get_feature_names())


model_linear02 = LinearRegression()
#y_model02 = model_linear02.fit(X[:, np.newaxis], y).predict(X2_polyFeat[:, np.newaxis])
y_model02 = model_linear02.fit(X_polyFeat, y).predict(X2_polyFeat)
print('Coeficentes: ',model_linear02.coef_)
print('y_intercept: ',model_linear02.intercept_)




# ----- usando make_pipeline
# Tem o mesmo efeito do código acima, exceto pelo parametro "degree" em PolynomialFeatures()

y_model03 = make_pipeline(PolynomialFeatures(degree=3), LinearRegression()).fit(X[:, np.newaxis], y).predict(X2[:, np.newaxis])

# ---- Plots

plt.scatter(X, y, color='black', label='Pontos-dados')
plt.plot(X2, y_model , label='Simples LinearRegression, degree = 1', lw=3)
plt.plot(X2, y_model02, color='green', label='LinearRegression degree = 5', lw=3)
plt.plot(X2, y_model03, color='r', label='LinearRegression degree = 3', lw=3)
plt.legend(loc='best')

#plt.savefig('PolynomialFeatures_AND_LinearRegression.png')
plt.show()
