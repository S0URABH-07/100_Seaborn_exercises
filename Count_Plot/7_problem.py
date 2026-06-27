# Count plot with common parameters
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(x="species", hue="island" ,order=["Chinstrap species","Adelie" ,"Gentoo"],data=load_data , legend=False , stat="percent")

plt.title("Customers Per Day")
plt.xlabel("Island")
plt.ylabel("Percent")
plt.grid(True)
plt.show()