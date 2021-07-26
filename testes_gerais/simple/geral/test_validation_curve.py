
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd

from sklearn.model_selection import validation_curve
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline

def make_data(size=100, seed=42, desv=0.6):
    rns = np.random.RandomState(seed)
    x = rns.rand(size)
    y = -1/(x + 0.1)
    if desv > 0:
        y += rns.randn(size)*desv
    return x, y

x, y = make_data()


# --- aplicando polynomialFeatures

model_poly_feat = PolynomialFeatures(degree=5)

x_poly = model_poly_feat.fit_transform(x[:, np.newaxis])

dataFrame_x = pd.DataFrame(x_poly, columns=model_poly_feat.get_feature_names())

#Data frame features polinomiais de x
print(dataFrame_x)


# --- aplicando LinearRegression

model_linear = LinearRegression()
model_L = model_linear.fit(x_poly, y)

#----- aplicando o modelo acima sobre novos dados

x_2 = np.linspace(0,1,500) # dados
x_2_poly = model_poly_feat.fit_transform(x_2[:, np.newaxis]) # aplicando PolynomialFeatures

y_x2_predict = model_L.predict(x_2_poly)



# ------- validation validation_curve
# Achando o melhor valor para o parâmetro degree

degree = np.arange(0,21) # intervalo de análise

model = make_pipeline(PolynomialFeatures(), LinearRegression())

#train_score: relacionado aos dados de treino (data_train)
#validation_score: relacionado aos dados e treino (data_test)
# desse modo a função validation_curve mostra a curva onde é possível
# observar onde o parametro, desse caso o "degree" faz uma melhor
# troca entre bias e variance.

train_score, validation_score = validation_curve(model, x[:, np.newaxis], y, param_name="polynomialfeatures__degree", param_range=degree, cv=5) # cv, cross validation splitt, para mais detalhes veja a referência 3

#plt.plot(degree, train_score, color='blue')
plt.plot(degree, np.median(train_score,1), color='red', label="train_score") # median com "1" significa que a mediana é feita pelas linhas, "0" para as colunas
plt.plot(degree, np.median(validation_score,1), color='green', label="Validation_score")
plt.title("Validation curve")
plt.xticks(np.arange(0,20))
plt.legend()
#plt.savefig('validation_curve_PolynomialFeatures_AND_LinearRegression.png')
plt.show()

# pelo gráfico pode-se perceber que o melhor degree que equilibra
# the bias and variance (underfitn and overfitn) está por volta do degree 4

# --- plots

#plt.scatter(x,y, label="Dados")
#plt.plot(x_2, y_x2_predict, color='r', lw=2.5, label="Linear Regression degree = 5")
#plt.legend(loc='best')

#plt.show()



# -- Referências

#[1] https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_bias_variance.html
#[2] https://jakevdp.github.io/PythonDataScienceHandbook/05.03-hyperparameters-and-model-validation.html
#[3] https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html
