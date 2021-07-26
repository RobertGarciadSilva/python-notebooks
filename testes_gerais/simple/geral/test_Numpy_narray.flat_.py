
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1,2,3],
                [4,5,6]])

x = np.linspace(0,1,100)

print(arr.shape)
print(list(arr.flat))

fig, axe = plt.subplots(2,2)

print(list(axe.flat))

#for i, ax in enumerate(axe.flat):
#    ax.scatter(x,x**i)

# Esse laço abaixo tem o mesmo efeito que o laço acima de duas linhas
exp = 0
for i in range(2):
    for j in range(2):
        axe[i][j].scatter(x, x**exp); exp +=1



plt.show()


# reference

#https://stackoverflow.com/questions/46862861/what-does-axes-flat-in-matplotlib-do
