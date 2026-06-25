# Bar plot and set ci (Confidence Interval)
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins").head(100)

order_1 = ["Dream","Torgersen" , "Biscoe"]
sns.barplot(x="island" , y="bill_length_mm" , data=load_data , hue="sex" , order=order_1 ,hue_order=["Female","Male"] , ci=100)
plt.show()