#Random Walk in three dimension
# This code don't is the better way to do plot 3D of Random Walk, see in file "3DimensionRandomWalkFile2.py" a better way.

from mpl_toolkits.mplot3d import axes3d #Usado para plotagem 3d
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

def three_dimension_random_walk(num_steps=100, plotar=False):
    x_path, y_path, z_path = [], [], []
    x_end, y_end, z_end = 0, 0, 0
    steps = [-1,1]
    for i in range(0, num_steps):
        x_path.append(random.choice(steps))
        y_path.append(random.choice(steps))
        z_path.append(random.choice(steps))
        x_end += x_path[i]
        y_end += y_path[i]
        z_end += z_path[i]

    # --- Utilizado apenas para definir xlim, ylim, zlim
    xMax, yMax, zMax = 0, 0, 0
    if(abs(x_end) > xMax):
        xMax = abs(x_end)
    if(abs(y_end) > yMax):
        yMax = abs(y_end)
    if(abs(z_end) > zMax):
        zMax = abs(z_end)
    #--------

    pathAndEnd = {'xPath':x_path, 'yPath':y_path, 'zPath':z_path, 'xEnd':x_end, 'yEnd':y_end, 'zEnd':z_end }
    if(plotar == False):
        return pathAndEnd
    else:

        # ----- PLOTAGEM
        xplot, yplot, zplot = [], [], []

        fig, ax = plt.subplots()
        fig.suptitle('Random walk 3 Dimension')
        ax = fig.add_subplot(111, projection='3d') # Definindo projeção 3d

        # Usado apenas para definir xlim, ylim, zlim
        axeMax = yMax
        if(xMax > yMax):
            axeMax = xMax
        if(zMax > axeMax):
            axeMax = zMax

        ax.set_xlim(-(axeMax+5),axeMax+5)
        ax.set_ylim(-(axeMax+5),axeMax+5)
        ax.set_zlim(-(axeMax+5),axeMax+5)

        # label axis
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')


        line, = ax.plot(xplot, yplot, zplot, 'g-')


        def init():
            line.set_data([], [])
            line.set_3d_properties([]) #eixo z
            return line,

        def update(i):
            xtemp, ytemp, ztemp = 0, 0, 0
            for m in range(0,i):
                xtemp += x_path[m]
                ytemp += y_path[m]
                ztemp += z_path[m]

            xplot.append(xtemp)
            yplot.append(ytemp)
            zplot.append(ztemp)
            line.set_data(xplot, yplot)
            line.set_3d_properties(zplot) #eixo z
            return line,

        an = animation.FuncAnimation(fig, update, init_func=init, frames=num_steps, interval=90, blit=True, repeat=False)

        #an.save('randomWalk3D.mp4', writer='ffmpeg', fps=30) #   Salvar animação

        plt.show()

        return pathAndEnd


randomWalk3Dimension = three_dimension_random_walk(1000, True)

#Saída padrão
print('XPath: ', randomWalk3Dimension['xPath'])
print('YPath: ', randomWalk3Dimension['yPath'])
print('ZPath ', randomWalk3Dimension['zPath'])
print('xEnd: ', randomWalk3Dimension['xEnd'])
print('yEnd: ', randomWalk3Dimension['yEnd'])
print('zEnd: ', randomWalk3Dimension['zEnd'])


#fontes:
# https://www.geeksforgeeks.org/graph-plotting-python-set-2/
# https://matplotlib.org/gallery/animation/simple_3danim.html
# https://stackoverflow.com/questions/53122090/trouble-animating-a-3d-plot-in-python
# https://stackoverflow.com/questions/38118598/3d-animation-using-matplotlib