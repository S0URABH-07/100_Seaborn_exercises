# Pair plot with kind with scatter parameter
# Scatter plot......Regression (best-fit) line
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data , hue="sex" ,kind="reg")
plt.show()