
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(10,10, figsize=(8,8),
                    subplot_kw={'yticks':[],'xticks':[]},
                    gridspec_kw={'hspace':0.5})

#fig.subplots_adjust(hspace=0.5)

#Observe que adicionar subplots_kw={'yticks':[],'xticks':[]}
#acima é equivalente a adicionar:
# ax.set_xticks([]) e ax.set_xticks([]) em cada plotagem

#observe também que adicionar gridspec_kw acima é equivalente
# a adicionar:
#fig.subplots_adjust(hspace=0.5)

for i, axe in enumerate(ax.flat):
#    axe.set_xticks([])
#   axe.set_yticks([])
    axe.text(0.05,0.05,str('nome'),
    color='red')

plt.show()
