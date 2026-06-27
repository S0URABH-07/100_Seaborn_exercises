# Horizontal Count Plot and split each category into another category
# A count plot shows how many times each category appears in a dataset
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(y="island", hue="sex",data=load_data)

plt.show()