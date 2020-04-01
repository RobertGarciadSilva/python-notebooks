# gerando números aleatórios e plotando algumas informações

import random
import numpy as np
import matplotlib.pyplot as plt


#função para gerar numeros aleatorios
def gera_data(n=100, min=0, max=100):
	data = []
	for i in range(min, max+1):
		data.append(random.randint(min, max+1))
	return data

data = gera_data()



#------- plot


fig, ax = plt.subplots(2,2, figsize=(10,6)) # determinando o objeto Figura e Axes; determina 4 subplots, [[ax1, ax2], [ax3,ax4]] 
fig.subplots_adjust(wspace=0.5, hspace=0.5) # epaçamento entre os subplots
fig.suptitle('Algumas plotagens de histogramas, para exemplo') # título da figura

# primeiro plot

ax[0][0].hist(data, bins=8, edgecolor='black') # define a plotagem do histograma com os dados; define a borda das barras como preta; bins: determina o número de barras, classes da plotagem.
ax[0][0].set_title('Distribuição de frequência') #definindo titulo
#ax[0][0].grid(axis='y', linestyle='-') # pode ser utilizado para plotar a grade sobre o eixo y
#ax[0][0].grid(axis='x', linestyle='-') # pode ser utilizado para plotar a grade sobre o eixo x
ax[0][0].spines['top'].set_visible(False) # define a linha horizontal do quadro do plot como Falsa
ax[0][0].spines['right'].set_visible(False) # define a linha horizontal do quadro do plot como Falsa


# segundo plot

ax[0][1].hist(data, bins=8, edgecolor='black', density=True) # define density como True, o que causa uma plotagem da distribuição relativa
ax[0][1].set_title('Distriuição de frequência relativa')
ax[0][1].spines['top'].set_visible(False)
ax[0][1].spines['right'].set_visible(False)

# terceiro plot

ax[1][0].hist(data, bins=8, edgecolor='black', cumulative=True, histtype='stepfilled') # define o plot como cumulativa e um segundo estilo de plotagem para histogramas.
ax[1][0].set_title('Distriuição acumulada')
ax[1][0].spines['top'].set_visible(False)
ax[1][0].spines['right'].set_visible(False)

# quarto plot

ax[1][1].hist(data, bins=8, edgecolor='black', log=True) # define eixo com escala logaritimica
ax[1][1].set_title("Distribuição escala logaritimica")
ax[1][1].spines['top'].set_visible(False)
ax[1][1].spines['right'].set_visible(False)


# display plotagem 

plt.show()

# Mais informações e parâmetros para plot.hist podem ser encontradas em:
#	https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html