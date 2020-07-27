
# some useful functions to EDA

from math import sqrt, floor
from numpy import arange, around

def createBinsIntHistogram(edgeMin, edgeMax, numReg=None, numBins=None, floor_ar=False):
    """Create edges integers list to histogram plot

    :parameter
    Or numReg or numBins need to be defined.

    edgeMin: int or float
            lowest sample value

    edgeMax: int or float
            higher sample value

    numReg: int
                number of samples
                if not passed, numBins will be used to estimate the size of the classes

    numBins: int
            number of classes,
            if not passed, sqrt (numRegistros) will be used to estimate the size of the classes.

    floor_ar: bool
        If True, the values to edges will be rounded to ceiling,
        false, the edges values will be rounded to floor

    :return: int list of edges


    Example:

    n = createBinsIntHistogram(4, 23.3, 36)
    Output: n = [ 4.  8. 12. 16. 20. 24.]

    n = createBinsIntHistogram(4, 23.3, 36, floor_ar=True)
    Output: n = [ 4.  7. 10. 13. 16. 19. 22.]

    References:

    [1]http://leg.ufpr.br/~fernandomayer/aulas/ce001e-2016-2/02_Analise_Exploratoria_de_Dados.html


    """

    amplitude = edgeMax - edgeMin
    if not numBins:
        numBins = sqrt(numReg)

    ampClass = amplitude/numBins

    if floor_ar:
        ampClass = floor(ampClass)
    else:
        ampClass = floor(ampClass +1)

    return arange(edgeMin, edgeMax +1, ampClass)









def label_densityHist(ax, n, bins, x=4, y=0.01, r=2, **kwargs):
    """
    Add labels,relative value of bin, to each bin in a density histogram .
    :param ax: Object axe of matplotlib
            The axis to plot.
    :param n: list, array of int, float
            The values of the histogram bins.
    :param bins: list, array of int, float
            The edges of the bins.
    :param x: int, float
            Related the x position of the bin labels. The higher, the lower the value on the x-axis.
            Default: 4
    :param y: int, float
            Related the y position of the bin labels. The higher, the greater the value on the y-axis.
            Default: 0.01
    :param r: int
            Number of decimal places.
            Default: 2
    :param **kwargs: Text properties in matplotlib
    :return: None


    Example

    import matplotlib.pyplot as plt
    import numpy as np

    dados = np.random.randn(100)

    axe = plt.gca()
    n, bins, _ = axe.hist(x=dados, edgecolor='black')
    label_densityHist(axe,n, bins)
    plt.show()

    Example:
    import matplotlib.pyplot as plt
    import numpy as np


    dados = np.random.randn(100)

    axe = plt.gca()
    n, bins, _ = axe.hist(x=dados, edgecolor='black')
    label_densityHist(axe,n, bins, x=6, fontsize='large')
    plt.show()


    Reference:
    [1]https://matplotlib.org/3.1.1/api/text_api.html#matplotlib.text.Text

    """

    k = []
    # calculate the relative frequency of each bin
    for i in range(0,len(n)):
        k.append((bins[i+1]-bins[i])*n[i])

    # rounded
    k = around(k,r); #print(k)

    # plot the label/text to each bin
    for i in range(0, len(n)):
        x_pos = (bins[i + 1] - bins[i]) / x + bins[i]
        y_pos = n[i] + (n[i] * y)
        label = str(k[i]) # relative frequency of each bin
        ax.text(x_pos, y_pos, label, kwargs)













# References

#[1]http://leg.ufpr.br/~fernandomayer/aulas/ce001e-2016-2/02_Analise_Exploratoria_de_Dados.html
#[2]https://matplotlib.org/3.1.1/api/text_api.html#matplotlib.text.Text






