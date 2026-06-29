# Box Plot with Professional Dashboard Style
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.figure(figsize=(13,7))

sns.boxplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    order=["Thur","Fri","Sat","Sun"],
    palette="coolwarm",
    width=0.55,
    linewidth=2,
    saturation=0.9,
    dodge=True,
    gap=0.2,
    fill=True,
    showfliers=True,
    fliersize=7
)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.show()