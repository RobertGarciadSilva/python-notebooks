
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

    x_path = []; #armazena todo o caminho x percorrido
    x_esperado = 0 #armazena a posição x final
    y_path = []; #armazena todo o caminho y percorrido
    y_esperado = 0 #armazena a posição y final

    maior_valor_absoluto_x = 0 #usado apenas para delimitar x_lim
    maior_valor_absoluto_y = 0 #usado apenas para delimitar y_lim

    steps = [-1,1]# passos possiveis
    for i in range(0, numSteps):
        x_path.append(random.choice(steps))
        y_path.append(random.choice(steps))
        x_esperado += x_path[i]
        y_esperado += y_path[i]

        #usados apenas para delimitar x_lim e y_lim
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
        ax = plt.gca() # "grabs the current axes", pega o atual objeto Axes
        ax.set_title('Random walk 2D')

        # utilizado apenas para se determinar qual eixo possui maior tamanho,
        # desse modo se determina axe_big, para que a plotagem fique simetrica em relação aos eixos x e y
        axe_big = maior_valor_absoluto_y
        if(maior_valor_absoluto_x > maior_valor_absoluto_y):
            axe_big = maior_valor_absoluto_x

        ax.set_xlim(-(axe_big+5), (axe_big+5)) #delimitando x_lim, aumentando seu tamanho somando o valor de 5, escolhido de forma arbitraria
        ax.set_ylim(-(axe_big+5), (axe_big+5)) #similar a linha acima para o eixo y

        line, = ax.plot(xdata, ydata, 'r-')

        tempx = 0
        tempy = 0

        for i in range(0, numSteps):
            xdata.append(tempx)
            ydata.append(tempy)
            line.set_xdata(xdata)
            line.set_ydata(ydata)
            plt.draw() #redesenha a plotagem
            plt.pause(1e-17) #pause entre as plotagens
            time.sleep(0.1) #pause na thread atual
            tempx += x_path[i]
            tempy += y_path[i]

        #plt.savefig('random_walk.png') # Utilizando para salvar o arquivo de plotagem/imagem, formato 'png', nome 'random_walk'
        plt.show()
        #-------------------------
        return x_esperado, y_esperado, x_path, y_path


x, y, xPath, yPath = two_dimension_random_walk(500, True)