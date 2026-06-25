# Bar plot horizontal 
# We have one condition if you draw plot horizontally you can want to use both axis numerically
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins").head(50)

order_1 = ["Dream","Torgersen" , "Biscoe"]
sns.barplot(x="bill_depth_mm" , y="bill_length_mm" , data=load_data ,orient="h")
plt.show()