
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def create_data(size=100, rseed=42, espalhamento=0.6):
    rms = np.random.RandomState(rseed)
    x = rms.rand(size,1)
    y = -1/(x.ravel() + 0.1) # função y = -1/(x + 0.1)
    if(espalhamento > 0):
        y += (rms.randn(size)*espalhamento)
    return x, y

X, y = create_data()

# --- As três declarações abaixo obtem o mesmo resultado
p = np.linspace(-1,1,10)[:, None]
p2 = np.linspace(-1,1,10)[:, np.newaxis]
p3 = np.linspace(-1,1,10).reshape(-1,1)
#print('P: ', p.shape)
#print('P2: ', p2.shape)
#print('P3: ', p3.shape)

x_lins = np.linspace(-0.1,1.1,500)

plt.scatter(X, y, color='black')
plt.plot(x_lins, -1/(x_lins + 0.1), color='red')
plt.xlim(-0.1,1)
plt.ylim(-12,1)

#plt.show()






print('----------------------------------------- testes')
arr = np.random.rand(2,2)

print('arr: ', arr)
print('arr.reshape(-1): ', arr.reshape(-1))
print('arr[:, np.newaxis]: ', arr[:, np.newaxis])
print('list(arr.flat): ', list(arr.flat))
print('arr.ravel(): ', arr.ravel())
