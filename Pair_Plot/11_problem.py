# Pair plot with plot_kws

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data ,hue="sex" , height=3 , aspect=3 , markers=["s","D"] , plot_kws={"alpha":0.5 , "s":60})
plt.show()