# A Factor Plot is a figure-level function that can create different categorical plots using a single interface.
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    kind="bar",
    palette="Set2",
    height=6,
    aspect=1.4,
    errorbar="sd"
)

g.set_axis_labels("Day", "Average Total Bill")
g.figure.suptitle("Average Total Bill by Day and Gender")

plt.show()