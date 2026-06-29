# Violin plot with styles
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(
    style="white",
    context="notebook",
    font_scale=1.1
)

plt.figure(figsize=(11,6))

sns.violinplot(
    x="day",
    y="total_bill",
    hue="sex",
    palette="coolwarm",
    split=True,
    inner="quart",
    data=tips
)

plt.title(
    "Total Bill Distribution",
    fontsize=18,
    color="navy",
    weight="bold"
)

plt.xlabel("Day", fontsize=14)
plt.ylabel("Total Bill", fontsize=14)

plt.show()