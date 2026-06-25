# Scatter plot with column category for label and diffrent color
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

load_data = sns.load_dataset("penguins")
sns.scatterplot(x="bill_length_mm" , y="bill_depth_mm" , data=load_data , hue="sex")
plt.show()