# Strip plot 
import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
sns.stripplot(x="day" , y="total_bill",hue="sex" , data=load_data)
plt.show()