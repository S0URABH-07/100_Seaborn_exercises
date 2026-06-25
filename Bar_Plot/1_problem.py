# Bar plot using seaborn
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins")
print(load_data)

sns.barplot(x=load_data.island , y=load_data.bill_length_mm , data=load_data)
plt.show()