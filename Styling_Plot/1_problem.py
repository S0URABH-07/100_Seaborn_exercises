# Box plot with style 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(
    style="darkgrid",
    palette="Set2",
    context="talk",
    font_scale=1.2
)

plt.figure(figsize=(10,6))

sns.boxplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    linewidth=2
)

plt.title("Professional Box Plot", fontsize=18, weight="bold")
plt.xlabel("Day", fontsize=14)
plt.ylabel("Total Bill", fontsize=14)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()