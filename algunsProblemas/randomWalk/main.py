
import matplotlib.pyplot as plt
import time
import random

import tkinter
matplotlib.use('TkAgg')

def one_dimension_random_walk(numSteps):
    walk = []
    posicaoEsperada = 0
    steps = [-1,1]
    for i in range(0, numSteps):
        walk.append(random.choice(steps))
        posicaoEsperada += walk[i]
    return walk, posicaoEsperada

def two_dimension_random_walk(numSteps):
    x_dimension = []; x_esperado = 0
    y_dimension = []; y_esperado = 0
    steps = [-1,1]
    for i in range(0, numSteps):
        x_dimension.append(random.choice(steps))
        y_dimension.append(random.choice(steps))
        x_esperado += x_dimension[i]
        y_esperado += y_dimension[i]
    return x_esperado, y_esperado

#------------------------------------------

xrange = []
for i in range(0,100):
    xrange.append(random.randrange(-50,50))

ysample = random.sample(xrange, 100)

xdata = []
ydata = []

plt.show()

axes = plt.gca()
axes.set_xlim(0, 100)
axes.set_ylim(-50, +50)
line, = axes.plot(xdata, ydata, 'r-')

for i in range(100):
    xdata.append(i)
ydata.append(ysample[i])
line.set_xdata(xdata)
line.set_ydata(ydata)
plt.draw()
plt.pause(1e-17)
time.sleep(0.1)

# add this if you don't want the window to disappear at the end
plt.show()