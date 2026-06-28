# Pair plot with diag_kind=kde 
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data , hue="sex" ,diag_kind="auto")
plt.show()