import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)


fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(7,8))
fig.subplots_adjust(hspace = 0.5) #espaçamento entre os subplots, neste caso está definindo a distancia vertical entre cada subplot


#plotagem função f(x) = sin(x), 0 a 4Pi
ax1.set_title('sin(x)') #definindo o titulo
ax1.set_xticks(np.arange(0, 4*np.pi,np.pi)) #define os valores do eixo x, espaçamento de Pi
ax1.grid(axis='y', linestyle='-') #coloca a grid no eixo y
ax1.grid(axis='x', linestyle='-') #coloca a grid no eixo x
ax1.plot(x, y, 'r-')


#plotagem função f(x) = cos(x)
ax2.set_title('cos(x)')
ax2.set_xticks(np.arange(0,4*np.pi, np.pi))
ax2.grid(axis='y', linestyle='-')
ax2.grid(axis='x', linestyle='-')
ax2.plot(x, y2, 'b-')


#plotagem sin(x) vs cos(x)
ax3.set_title('sin(x) vs cos(x)')
ax3.set_xticks(np.arange(0,4*np.pi, np.pi))
ax3.grid(axis='x', linestyle='-')
ax3.grid(axis='y', linestyle='-')
ax3.plot(x, y, 'r-', label=('sin(x)')) #definindo plotagem e a label para legenda
ax3.plot(x, y2, 'b-', label=('cos(x)'))
ax3.legend(loc=(0.82, 0.6)) #definindo a legenda, é baseada nas "labels" adiconado nos plots
plt.show()
