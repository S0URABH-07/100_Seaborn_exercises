# Change fontsize or color of annot using annot_kws
# Remove lavels of x and y axis
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("penguins").drop(["species","island","sex"] , axis=1).head(10)

fontcolor = {"fontsize":10 , "color":"r"}
sns.heatmap(load_data,annot=True ,vmin=0,vmax=2000 ,linewidths=2, linecolor="r", annot_kws=fontcolor ,xticklabels=False , yticklabels=False)
plt.show()