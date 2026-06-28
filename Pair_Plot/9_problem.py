# Pair plot with corner
# Only the lower triangle is displayed.
# This makes the plot cleaner and faster 

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

load_data = sns.load_dataset("tips")
sns.pairplot(load_data ,corner=True)
plt.show()