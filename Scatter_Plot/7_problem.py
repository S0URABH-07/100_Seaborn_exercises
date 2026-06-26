# Scatter plot with markers change
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

load_data = sns.load_dataset("penguins")

marker = {"Male":"*" , "Female":"o"}
sns.scatterplot(x="bill_length_mm" , y="bill_depth_mm" , data=load_data , hue="sex", style="sex",palette="PuBu" , markers=marker)
plt.show()