# Box plot with Publication-Quality Styling
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(
    style="whitegrid",
    palette="deep",
    context="paper",
    font_scale=1.1
)

plt.figure(figsize=(12,6))

sns.boxplot(
    x="day",
    y="total_bill",
    hue="smoker",
    data=tips,
    linewidth=2
)

plt.title(
    "Publication Quality Box Plot",
    fontsize=18,
    weight="bold"
)

plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.legend(
    title="Smoker",
    loc="upper left"
)

plt.grid(alpha=0.25)

sns.despine()

plt.tight_layout()

plt.show()