# Add title,grid etc..
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=load_data,hue="sex")
plt.title("Line Plot",fontdict={"fontsize":20})
plt.grid()
plt.show()