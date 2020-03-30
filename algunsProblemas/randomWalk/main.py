
import matplotlib
import matplotlib.pyplot as plt
import time
import random

matplotlib.use('TkAgg')

def one_dimension_random_walk(numSteps):
    walk = []
    posicaoEsperada = 0
    steps = [-1,1]
    for i in range(0, numSteps):
        walk.append(random.choice(steps))
        posicaoEsperada += walk[i]
    return walk, posicaoEsperada

def two_dimension_random_walk(numSteps, plotar = False):
    x_path = []; x_esperado = 0
    y_path = []; y_esperado = 0
    maior_valor_absoluto_x = 0
    maior_valor_absoluto_y = 0

    steps = [-1,1]
    for i in range(0, numSteps):
        x_path.append(random.choice(steps))
        y_path.append(random.choice(steps))
        x_esperado += x_path[i]
        y_esperado += y_path[i]

        if(abs(x_esperado) > maior_valor_absoluto_x):
            maior_valor_absoluto_x = abs(x_esperado)
        if(abs(y_esperado) > maior_valor_absoluto_y):
            maior_valor_absoluto_y = abs(y_esperado)

    if(plotar == False):
        return x_esperado, y_esperado, x_path, y_path

    else:
        #-- Exibe informações na saída padrao
        print('[X, Y] = [',x_esperado,',',y_esperado,']')
        print('Path X = ', x_path)
        print('Path Y = ', y_path)

        # -- PLOTAGEM
        xdata = []
        ydata = []

        plt.show()
        ax = plt.gca()
        ax.set_xlim(-(maior_valor_absoluto_x+5), (maior_valor_absoluto_x+5))
        ax.set_ylim(-(maior_valor_absoluto_y+5), (maior_valor_absoluto_y+5))

        line, = ax.plot(xdata, ydata, 'r-')

        tempx = 0
        tempy = 0

        for i in range(0, numSteps):
            xdata.append(tempx)
            ydata.append(tempy)
            line.set_xdata(xdata)
            line.set_ydata(ydata)
            plt.draw()
            plt.pause(1e-17)
            time.sleep(0.1)
            tempx += x_path[i]
            tempy += y_path[i]

        plt.show()
        #-------------------------
        return x_esperado, y_esperado, x_path, y_path


x, y, xPath, yPath = two_dimension_random_walk(500, True)