
# 3D random Walk e plotagem

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3    # biblioteca usada para projection 3D



def gera_randomLine(dims=3, length=10):
    '''
    Gera o caminho aleatorio em um sistema com dims dimensões de comprimento length.
    :param dims: Dimenão do random walk, nesse caso definido por padrão trẽs dimensões [x, y, z].
    :param length: Comprimento da caminhada, walk.
    :return: Lista de listas, em que cada lista represena uma dimensão.
    '''
    lineData = np.empty((dims, length)) # Cria array vazio com dims linhas e length colunas.
    lineData[:,0] = np.random.rand(dims) # Preenche de forma aleatoria a primeira coluna do array anteriormente criado. [:,0] representa todas as linhas da coluna 0.
    for i in range(1,length): # preenche apartir da posição 1 as colunas do array anteriormente criado, a posição 0 já foi preenchida na linha acima.
        step = ((np.random.rand(dims) - 0.5) * 0.1) # Passos. Observe que a subração por 0.5 faz com que os valores aleatorios de np.random.rand() variem entre [-0.5,0.5), 0.1 é um valor arbitrario mas que deve ser pequeno
                                                    # para representar pequenas variações nos passos.
        lineData[:,i] = lineData[:, i-1] + step # Preenche o array com as dimensões, cada linha sendo uma lista representando uma dimensão.
    return lineData


def update(i, dados, lines):
    '''
    Função de atualização da plotagem, chamada para cada número no valor de frames definido em animation.
    :param i: Paramẽtro de atualização dos frames. Repare que i funciona como em um laço for ( for i in range(0, numero_de_frames)).
    :param dados: Dados para plotagem.
    :param lines: Objeto line, axe.plot, para plotagem.
    :return:
    '''
    for line, data in zip(lines, dados):
        line.set_data(dados[0:2,:i])    # [0:2,:i] representa as linhas 0 e 1, dimensão x, y, do array dados com as colunas até i.
        line.set_3d_properties(dados[2, :i]) # [2, :i], representa a linha 2, dimensão z, do array dados com colunas até i.
    return lines


def plot_random_walk_3D(numSteps=100):
    '''
    Plotagem random_Walk 3D
    :param numSteps: Número de passos, walk.
    :return:
    '''

    fig = plt.figure()
    ax = p3.Axes3D(fig)     # Definindo objeto Axe para plotagem 3D.
    fig.suptitle('Random Walk 3D')

    data = gera_randomLine(3,numSteps)  #Gerando dados, nesse caso para 3 dimensões (x, y, z). Cada linha da data representando uma dimensão com numSteps de passos.
    line = ax.plot(data[0,0:1],data[1,0:1],data[2,0:1], 'r-') # Criando objeto line, ax.plot.
    # data[0,0:1] linha x do array data, representa eixo x, pegando coluna 0.
    # Observe  a diferença entre [0,0] e [0,0:1]: [0,0] retorna um x e [0,0:1] retorna um [x], ou seja, o a segunda forma retorna um valor dentro de uma lista.
    # data[0,0] -> valor da linha 0 e coluna 0 de data
    # data[0,0:1] -> valor da linha 0 e coluna de 0 até 1 de data.

    #-- Definindo limites dos eixos e as labels.
    ax.set_xlim3d([0,1])
    ax.set_xlabel('x')

    ax.set_ylim3d([0,1])
    ax.set_ylabel('y')

    ax.set_zlim3d([0,1])
    ax.set_zlabel('z')

    #Função para animação.
    an = animation.FuncAnimation(fig, update, frames=numSteps, fargs=(data,line), interval=90, blit=False, repeat=False)
    #an.save('3DimensionRandomWalkFile2.mp4', writer='ffmpeg', fps=30) # Salvar animação
    plt.show()

plot_random_walk_3D(500)



# ------  Fontes:

#   https://matplotlib.org/1.4.1/examples/animation/simple_3danim.html
#   https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html
#   https://stackoverflow.com/questions/38118598/3d-animation-using-matplotlib