
import numpy as np
import matplotlib.pyplot as plt
import random


def geraDados(plot_range,numDots=100):
    '''
    Gera valores aleatórios x e y de modo que seguem uma tendência linear. Define uma lista 'category' arbitrária
    de modo que para cada par [x, y] é definida uma categoria: 0 ou 1, arbitrário. Essa lista 'category' é usada
    apenas para exemplo de plotagem scatter com pontos representando categorias.
    :param plot_range: Dicionario com faixa de valores do eixo x, [xMin, xMmax]
    :param numDots: Numero de pontos a serem plotados
    :return: Lista x e lista y contendo os pontos para plotagem e lista 'category' contendo a categoria para
    cada ponto [x,y].
    '''
    x, y, category = [], [], []
    cat = [0,1]
    for i in range(0,numDots):
        x_rand = random.randrange(plot_range['xMin'], plot_range['xMax']+1)
        y_rand = random.randrange(x_rand-15, x_rand+15) # y_rand é definido desse modo para seguir uma tendência linear. Observe que os valores de y são definidos apartir dos valores de x. 15 é um valor arbitrário.
        x.append(x_rand)
        y.append(y_rand)
        category.append(random.choice(cat))
    return x, y, category

def plotScatter(x, y, category):
    '''
    Plotagem scatter dos dados em pares [x,y] em que cada par possoi uma categoria (0 ou 1) definida em 'category'.
    :param x: Lista com os dados para o eixo em x.
    :param y: Lista com os dados para o eixo em y.
    :param category: Categoria (0 ou 1) de cada par [x,y].
    :return:
    '''
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.suptitle('X vs Y Scatter')

    color_category = ['#2300A8', '#00A658'] # cores para as categorias, #2300A8 representa a categoria 0 e #00A658 representa a categoria 1.
    categories = ['0', '1'] # label para as categorias, usado para definir as legendas.

    #Observe que o modo feito abaixo, usando "for" com "ax.scatter" é plotado cada ponto separadamente.
    for i in range(0, 100):
        if (category[i] == 0):
            ax.scatter(x[i], y[i], alpha=0.70, color=color_category[0], label=categories[0])    # alpha representa a transparência dos pontos. Categoria 0.
        elif (category[i] == 1):
            ax.scatter(x[i], y[i], alpha=0.70, color=color_category[1], label=categories[1])    # categoria 1.

    # Define as labels x, y e remove as spines do topo e da direita
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # adiciona a grade no plot, linewidth representa o espaçamento entre as linhas da grade, alpha representa a transparência.
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.9)

    #legenda. "np.unique" é usado para pegar os valores unicos defindos nas labels. Se necessário teste definindo "ax.legend()" ou "ax.legend(categories)". Veja referência [3]
    ax.legend(np.unique(categories))

    #plt.savefig('exemploPlotScatter.png') # salvar plotagem
    plt.show()



plot_range = {'xMin':0,'xMax':100} # Dicionário com valores de min e max para os valores do eixo x.
x, y, category = geraDados(plot_range, 100) #Dados [x,y] com categoria definida em 'category'.
plotScatter(x, y, category) #Plotagem scatter


# Referências
#   [1] https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f
#   [2] https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.scatter.html
#   [3] https://www.geeksforgeeks.org/python-get-unique-values-list/
#   [4] https://www.geeksforgeeks.org/python-pandas-dataframe-ix/
