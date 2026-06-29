# Catplot with points plot 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    kind="point",
    palette="Set2",
    height=6,
    aspect=1.4
)

g.set_axis_labels("Day", "Average Total Bill")
g.figure.suptitle("Average Total Bill by Day and Gender")

plt.show()