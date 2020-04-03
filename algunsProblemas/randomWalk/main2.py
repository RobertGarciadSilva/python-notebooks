
# random walk in two and three dimension using plot animation

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

        if(abs(x_end) > x_mod):
            x_mod = abs(x_end)
        if(abs(y_end) > y_end):
            y_mod = y_end

    if(plotagem == False):
        return x_walk, y_walk, x_end, y_end
    else:
        # ------------- plot
        xplot, yplot = [], []

        fig, ax = plt.subplots(1,1)
        fig.suptitle('Plotagem random walk using plot animation')

        axis_big = x_mod
        if y_mod > x_mod:
            axis_big = y_mod

        ax.set_xlim(-(axis_big + 5),(axis_big + 5))
        ax.set_ylim(-(axis_big + 5),(axis_big + 5))

        line, = ax.plot(xplot, yplot, 'b-')

        def init():
            line.set_data([], [])
            return line,

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
        #an.save('random_walk.mp4', writer='ffmpeg', fps=30)
        plt.show()

        return x_walk, y_walk, x_end, y_end


xPath, yPath, x, y = randdom_walk_two_dimensions(1000, plotagem=True)

# Impressão na saída padrão
print('Walk X: ', xPath)
print('Walk Y: ', yPath)
print('X end: ', x)
print('Y end: ', y)




