# Bar plot and change ci width
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins").head(100)

order_1 = ["Dream","Torgersen" , "Biscoe"]
sns.barplot(x="island" , y="bill_length_mm" , data=load_data , hue="sex" , order=order_1 ,hue_order=["Female","Male"], err_kws={"linewidth":5})
plt.show()