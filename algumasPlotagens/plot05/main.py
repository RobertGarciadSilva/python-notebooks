

#imports
from pandas import DataFrame
import matplotlib.pyplot as plt



# data used to plots

data01 = {'Unemploymente_Rate':[6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2], 
		  'Stock_Index_Price':[1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]}


data02 = {'Year':[1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
		  'Unemploymente_Rate':[9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]}



data03 = {'Country':['USA','Canada','Germany','UK', 'France'],
		  'GDP_Per_Capita':[45000,42000,52000,49000,47000]}


data04 = {'Tasks':[300,500,700]}
data04 = DataFrame(data04, columns=['Tasks'], index=['Tasks Pending', 'Tasks Ongoing', 'Tasks Completed'])




#plot scatter
def plot_scatter(data, x_axis, y_axis, save=False, plot=True, **args):
	if(type(data) != 'DataFrame'):
		data = DataFrame(data, columns=[x_axis, y_axis])
	

	data.plot(x=x_axis, y=y_axis, kind='scatter')
	plt.title(y_axis + ' by ' + x_axis)

	if(save == True):
		if(len(args) >= 1):
			plt.savefig(args['name_fig'] + '.png')
		else:
			plt.savefig('plot_scatter.png')

	if(plot == True):
		plt.show()



# plot line
def plot_line(data, x_axis, y_axis, save=False, plot=True, **args):
	if(type(data) != 'DataFrame'):
		data = DataFrame(data, columns=[x_axis, y_axis])

	data.plot(x=x_axis, y=y_axis, kind='line')
	plt.title(y_axis + ' by ' + x_axis)

	if(save == True):
		if(len(args) >= 1):
			plt.savefig(args['name_fig'] + '.png')
		else:
			plt.savefig('plot_line.png')

	if(plot == True):
		plt.show()


#plot bar
def plot_bar(data, x_axis, y_axis, save=False, plot=True, **kargs):
	if(type(data) != 'DataFrame'):
		data = DataFrame(data, columns=[x_axis, y_axis])

	data.plot(x_axis, y_axis, kind='bar', color='red')
	plt.title(x_axis + ' by ' + y_axis)

	if(save == True):
		if(len(kargs) >= 1):
			plt.savefig(kargs['name_fig']+'.png')
		else:
			plt.savefig('plot_bar.png')

	if(plot == True):
		plt.show()	



#plot pie
def plot_pie(data, save=False, plot=True, **kargs):
	
	data.plot.pie(y='Tasks', autopct='%1.1f%%', startangle=90)
	plt.title('Tasks')
	plt.legend(loc=(0.86, 0.8))
	
	if(save == True):
		if(len(kargs) >= 1):
			plt.savefig(kargs['name_fig']+'.png')
		else:
			plt.savefig('plot_pie.png')


	if(plot == True):
		plt.show()



if(__name__ == '__main__'):
	plot_scatter(data01, 'Unemploymente_Rate', 'Stock_Index_Price', save=True, name_fig='scatter_plot')
	plot_line(data02, 'Year', 'Unemploymente_Rate', save=True)
	plot_bar(data03, 'Country', 'GDP_Per_Capita', save = True, name_fig='plot_bar_exemple.png')
	plot_pie(data04, save=True)









# References

#	[1]https://datatofish.com/plot-dataframe-pandas/