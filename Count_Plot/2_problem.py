# Horizontal Count Plot 
# A count plot shows how many times each category appears in a dataset
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(y="island", data=load_data)

plt.show()