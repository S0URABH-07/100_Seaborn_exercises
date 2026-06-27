# Horizontal Violin plot and Split each violin into another category using hue
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="bill_length_mm",y="species", hue="island",data=load_data)

plt.show()