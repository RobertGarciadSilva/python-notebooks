import matplotlib
matplotlib.use('Agg') # Indica que o script será rodado em um ambiente não grafico (servidor)
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline #Objeto BSpline

#Obtendo dados do arquivo
arquivo = open("input.txt","r")
stringDados = arquivo.readline()
arquivo.close()

stringDados = stringDados.replace(",",".")
stringDados = stringDados.split(";")
dadosX = stringDados[0].split(" ")
dadosY = stringDados[1].split(" ")

concentracao = []
inibicao = []



for i in dadosX:
    concentracao.append(float(i))

for i in dadosY:
    inibicao.append(float(i))

np.array(concentracao)
np.array(inibicao)

concentracao = np.sort(concentracao) #array np dos dados eixo x
inibicao = inibicao[::-1] # invertendo o array y


xnew = np.linspace(concentracao.min(), concentracao.max(), 300) # 300 representa o numero de pontos plotados.
spl = make_interp_spline(concentracao, inibicao, k=3) # cria objeto BSpline
y_smooth = spl(xnew)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# edita os eixos para o sistema de coordenas ficar centralizado na plotagem
ax.spines['left'].set_position(('data',0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# edita as legendas dos eixos x y
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylabel(" % Inibição")
ax.set_xlabel("Ln (Concentração NP)")
ax.xaxis.set_label_coords(0.5, 0)
ax.yaxis.set_label_coords(0, 0.6)

# plotagem
plt.plot(xnew,y_smooth)
figura = plt.gcf() # Salva a figura corrente, gcf() "get current figure"
#plt.show()
figura.savefig("graficoDados.png", format="png")
outPutString = ""\
+ "<Activity>\n"\
+ " <attributes class=\"linked-hash-set\">\n"\
+ "	<File xpdlId=\"plotImg\">\n"\
+ "		<value>graficoDados.png</value>\n"\
+ "	</File>\n"\
+ " </attributes>\n"\
+ "</Activity>"


print(outPutString)
