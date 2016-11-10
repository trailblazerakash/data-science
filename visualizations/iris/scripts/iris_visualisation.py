import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("../Iris.csv")
#first pyplot
fig = iris.plot(kind='scatter',x='SepalWidthCm',y='SepalLengthCm')
fig = fig.get_figure()
fig.savefig("../outputs/scatter1.png")
#scatter with hues
fig = sns.FacetGrid(iris,hue='Species',size=10).map(plt.scatter,'SepalLengthCm','SepalWidthCm').add_legend()

fig.savefig("../outputs/scatter_with_hue.png")
fig = sns.FacetGrid(iris,hue='Species',size=10).map(plt.scatter,'PetalLengthCm','PetalWidthCm').add_legend()
fig.savefig("../outputs/scatter_with_hue2.png")

print "development of Box plot"

fig= sns.boxplot(x='Species',y="PetalLengthCm",data=iris)
fig = fig.get_figure()
fig.savefig("../outputs/box_plot1.png")

fig= sns.boxplot(x='Species',y="SepalLengthCm",data=iris)
fig = fig.get_figure()
fig.savefig("../outputs/box_plot2.png")
fig= sns.boxplot(x='Species',y="SepalWidthCm",data=iris)
fig = fig.get_figure()
fig.savefig("../outputs/box_plot2.png")
fig= sns.boxplot(x='Species',y="PetalWidthCm",data=iris)
fig = fig.get_figure()
fig.savefig("../outputs/box_plot2.png")
print "kde plot"

fig = sns.FacetGrid(iris,hue='Species',size=10).map(sns.kdeplot,'PetalLengthCm').add_legend()
fig.savefig("../outputs/kdeplot.png")


#pairplot

fig = sns.pairplot(iris.drop("Id",axis=1),hue='Species',size=5)
fig.savefig("../outputs/pairplot.png")
