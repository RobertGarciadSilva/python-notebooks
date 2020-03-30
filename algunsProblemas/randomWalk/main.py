
import random

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



x, y = two_dimension_random_walk(100)
print('x: ', x, 'y: ', y)