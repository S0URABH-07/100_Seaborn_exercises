# Violin plot with inner parameter
# inner -> Controls what appears inside the violin 
        # inner="box" -> Shows a mini box plot.
        # inner="quart" -> Shows the 25th, 50th, and 75th percentiles
        # inner="points" -> Shows inner data points
        # inner="stick" -> Every observation is shown as a small line
        # inner="None" -> Blank Violin plot

import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="species", y="bill_length_mm",data=load_data  ,inner="stick")

plt.show()