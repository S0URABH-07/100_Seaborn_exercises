# Pair plot with kind with hist parameter
# Histograms are used in the off-diagonal cells instead of scatter plots.
# You want to compare distributions rather than point-by-point relationships.
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data , hue="sex" ,kind="hist")
plt.show()