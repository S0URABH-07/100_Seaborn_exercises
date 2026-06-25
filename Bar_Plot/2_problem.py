# Bar plot using hue for male and female both
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins")

sns.barplot(x="island" , y="bill_length_mm" , data=load_data , hue="sex")
plt.show()