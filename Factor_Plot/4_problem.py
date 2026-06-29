# Violin plot with partition using catplot with col parameter
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)
g = sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="violin",
    split=True,
    inner="quart",
    palette="coolwarm",
    height=5,
    aspect=1
)

g.figure.suptitle("Lunch vs Dinner")

plt.show()