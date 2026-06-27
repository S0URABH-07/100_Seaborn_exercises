# Violin plot split with male and female category
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="species", y="bill_length_mm",hue="sex",data=load_data,split=True)

plt.show()