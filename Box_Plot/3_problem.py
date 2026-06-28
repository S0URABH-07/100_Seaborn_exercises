# Advanced Box Plot with Hue & Gap
# gap -> Adds extra space between hue groups, making them easier to distinguish 
# fill -> Displays filled boxes instead of outlines only.
# fliersize-> Makes outlier points larger and easier to notice.
# hue , dodge
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.figure(figsize=(11,6))

sns.boxplot(
    x="day",
    y="total_bill",
    hue="smoker",
    data=tips,
    palette="viridis",
    width=0.65,
    linewidth=2,
    dodge=True,
    gap=0.15,
    fill=True,
    fliersize=6
)

plt.title("Total Bill by Smoker Status")
plt.legend(title="Smoker")

plt.show()