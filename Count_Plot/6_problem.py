# Count plot without legend and use stat
# dodge ->Bars appear side by side
# A count plot shows how many times each category appears in a dataset
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(x="species", hue="island" ,order=["Chinstrap species","Adelie" ,"Gentoo"],data=load_data , legend=False , stat="percent")

plt.show()