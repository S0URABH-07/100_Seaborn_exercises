# Violin plot with cut
# Controls how far the KDE extends beyond the minimum and maximum values
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="species", y="bill_length_mm",data=load_data,cut=3 )

plt.show()