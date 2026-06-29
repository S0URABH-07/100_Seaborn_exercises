# Bar plot and Styling with rc Parameters
# rc lets you customize many Matplotlib settings in one place
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(
    style="ticks",
    rc={
        "axes.facecolor":"#F7F7F7",
        "axes.edgecolor":"black",
        "grid.linestyle":"--",
        "grid.alpha":0.4
    }
)

plt.figure(figsize=(10,6))

sns.barplot(
    x="day",
    y="total_bill",
    hue="time",
    data=tips,
    palette="viridis"
)

plt.title("Average Total Bill")

sns.despine()

plt.show()