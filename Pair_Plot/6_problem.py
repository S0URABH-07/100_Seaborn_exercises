# Pair plot with kind with kde parameter
# Instead of dots, Seaborn draws density contours.
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data , hue="sex" ,kind="kde")
plt.show()