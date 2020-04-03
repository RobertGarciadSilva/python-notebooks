
# random walk in two dimension using plot animation

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randdom_walk_two_dimensions(num_steps=100, plotagem=False):
    x_walk = []; y_walk = []
    x_end = 0; y_end = 0
    x_mod, x_mod = 0, 0
    step = [-1,1]
    for i in range(0,num_steps):
        x_walk.append(random.choice(step))
        y_walk.append(random.choice(step))
        x_end += x_walk[i]
        y_end += y_walk[i]

        # usando apenas para a definição de xlim e ylim
        if(abs(x_end) > x_mod):
            x_mod = abs(x_end)
        if(abs(y_end) > y_mod):
            y_mod = abs(y_end)

    if(plotagem == False):
        return x_walk, y_walk, x_end, y_end
    else:

        # ---------------- plot
        xplot, yplot = [], []

        fig, ax = plt.subplots(1,1)
        fig.suptitle('Plotagem random walk using plot animation')

        #usado apenas para a definição de xlim e ylim, de modo que fiquem simetricos
        axis_big = x_mod
        if y_mod > x_mod:
            axis_big = y_mod

        ax.set_xlim(-(axis_big + 5),(axis_big + 5))
        ax.set_ylim(-(axis_big + 5),(axis_big + 5))

        line, = ax.plot(xplot, yplot, 'b-')

        #função de inicialização da animação
        def init():
            line.set_data([], [])
            return line,

        #função de atualização da animação
        def update(i):
            xtemp, ytemp = 0,0
            for m in range(0,i):
                xtemp += x_walk[m]
                ytemp += y_walk[m]

            xplot.append(xtemp)
            yplot.append(ytemp)
            line.set_data(xplot, yplot)

            return line,

        an = animation.FuncAnimation(fig, update, init_func=init, frames=num_steps, interval=60, blit=True, repeat=False)
        #Objeto para a realiação da animação.
        #   - fig é o objeto onde será plotado
        #   - init_func, parâmetro que realiza a chamada da função inicial para a plotagem da animação
        #   - update é a função que será chamada para a atualização dos frames,
        #   repare que essa função conta com o parâmetro "i", que nesse caso é apenas um iterador,
        #   no presente caso seu valor é iniciado, de forma automatica, como 0 e seu limite é determinado
        #   pelo parâmetro "frames".
        #   - frames: determinado o número de frames/quadros/chamada a função update da animação
        #   - interval: tempo, em milisegundos, para a chamadada função "update", ou seja, tempo para a atualização
        #   - repeate: determinada se a animação irá ficar repetindo-se ou não.
        #   - blind: setting blit=True means that only those parts will be drawn, which have changed.
        #   Mais informações e exemplos podem ser encontradas em:
        #   - https://www.geeksforgeeks.org/graph-plotting-python-set-3/?ref=rp
        #   - https://matplotlib.org/3.1.1/api/animation_api.html

        #an.save('random_walk.mp4', writer='ffmpeg', fps=30)
            #usado para salvar o arquivo com a animação:
            #   - "random_walk.mp4" é o nome do arquivo com o formato mp4
            #   - ffmpeg é o escritor de arquivo de midia, pode ser necessário a instalação desse pacote 'ffmpeg' na maquina
            #   - Mais informações em: https://www.edivaldobrito.com.br/ffmpeg-no-debian-ubuntu-e-fedora/

        plt.show()

        return x_walk, y_walk, x_end, y_end

#chamada a função
xPath, yPath, x, y = randdom_walk_two_dimensions(1000, plotagem=True)

# Impressão na saída padrão
print('Walk X: ', xPath)
print('Walk Y: ', yPath)
print('X end: ', x)
print('Y end: ', y)




