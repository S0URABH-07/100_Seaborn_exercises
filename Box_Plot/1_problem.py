# Box plot with multiple parameters
# it shows->> Minimum, First Quartile (Q1), Median (Q2), Third Quartile (Q3), Maximum, Outliers
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.figure(figsize=(10,6))

sns.boxplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="Set2",
    width=0.4,
    linewidth=2,
    saturation=0.8,
    dodge=True
)

plt.title("Total Bill Distribution by Day and Gender", fontsize=15)
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.grid(alpha=1)

plt.show()