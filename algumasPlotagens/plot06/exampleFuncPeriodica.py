
import numpy as np
import matplotlib.pyplot as plt

# f(x) tal que f(x) = cos(x) para -2 <= x < 2 e f(x) = f(x + 4) para todo x pertencente aos reais.

def f(x):
	return np.cos(x)


x = np.linspace(-6,6,200)
y = []

for a in x:
	if(a >= -2 and a < 2):
		y.append(f(a))
	else:
		# fazendo a correção f(x) = f(x + 4), 4 = T, período
		n = (a/4)
		n = round(n)
		b = a - n*4
		y.append(f(b))

fig, axe = plt.subplots()

axe.spines['left'].set_position('center')
axe.spines['bottom'].set_position('center')

axe.spines['right'].set_color('none')
axe.spines['top'].set_color('none')


axe.xaxis.set_ticks_position('bottom')
axe.yaxis.set_ticks_position('left')

#axe.set_xticks(np.arange(-10,10,2))

axe.plot(x,y, color='red')
axe.set_title('f(x) tal que f(x) = cos(x) para -2 <= x < 2 e f(x) = f(x + 4) para todo x pertencente aos reais', size=8)
axe.set_xlabel('x')
axe.set_ylabel('y')
plt.savefig('exampleFuncPeriodica.png')
#plt.show()


