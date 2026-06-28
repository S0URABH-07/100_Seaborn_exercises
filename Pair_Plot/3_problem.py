# Pair plot with other parameters
# Using vars you can draw graphs according to you
# Hue_order use for pattern order first female than man
# palette= for color change
# x_vars= used for x axis used column. Only these column used for plot
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data , hue="sex" , vars=["tip" , "total_bill" ] ,hue_order=["Female","Male"] , palette="BuGn" , x_vars=["total_bill" , "tip"])
plt.show()