# Box plot with Strip plot 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.figure(figsize=(12,6))

sns.boxplot(
    x="day",
    y="total_bill",
    data=tips,
    linewidth=1,
    linecolor="black",
    fill=True,
    width=0.5,
    showfliers=False
)

sns.stripplot(
    x="day",
    y="total_bill",
    data=tips,
    color="red",
    jitter=True,
    linewidth=1,
    size=8
)

plt.show()