# Scatter plot with color change
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

load_data = sns.load_dataset("penguins")
sns.scatterplot(x="bill_length_mm" , y="bill_depth_mm" , data=load_data , hue="sex", style="sex",size="sex",sizes=(50,20) , palette="PuBu")
plt.show()