# Draw horizontal and change color using palette
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins").head(50)

order_1 = ["Dream","Torgersen" , "Biscoe"]
sns.barplot(x="bill_depth_mm" , y="bill_length_mm" , data=load_data ,orient="h" ,hue="sex" , palette='PuBu')
plt.show()