
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import os

def ger_data01(size=100, min=0, slope=2, intercept=-5, disper=1.2, max=1, **kargs):
    rs = np.random.RandomState(10)
    x = max*rs.rand(size) + min

    if('slope' in kargs and 'intercept' in kargs):
        slope = kargs['slope']
        intercept = kargs['intercept']

    y = slope*x + intercept + (rs.random(size)*disper)

    return x, y


def show_scatterData(x, y):
    plt.scatter(x, y, color='r')
    plt.show()


def save_data(data):
    path = os.path.dirname(__file__)
    os.chdir(path)
    data.to_csv(r'./data01.csv', index=False, header=True)

if(__name__ == '__main__'):
    x, y = ger_data01(slope=6, intercept=3);
    data = {'x':x,'y':y}
    dfData = pd.DataFrame(data)
    save_data(dfData)
    show_scatterData(x, y)



#references

# https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html
# https://note.nkmk.me/en/python-script-file-path/
# https://www.it-swarm.dev/pt/python/chame-uma-funcao-de-outro-arquivo-em-python/1042916572/
# https://stackoverflow.com/questions/22994423/difference-between-np-random-seed-and-np-random-randomstate
