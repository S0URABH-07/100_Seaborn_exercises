# Violin plot with Controls violin width using density_norm=
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="species", y="bill_length_mm",data=load_data, density_norm="width" )

plt.show()