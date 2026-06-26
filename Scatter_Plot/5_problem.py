# Scatter plot with change style size 
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

load_data = sns.load_dataset("penguins")
sns.scatterplot(x="bill_length_mm" , y="bill_depth_mm" , data=load_data , hue="sex", style="sex",size="sex",sizes=(100,20))
plt.show()