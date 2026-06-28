# Horizontal Box Plot with Ordering
# USE -> order , palette ,width ,linewidth ,showfliers ,orient
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
plt.figure(figsize=(11,6))

sns.boxplot(
    y="day",
    x="tip",
    hue="sex",
    data=tips,
    order=["Thur","Fri","Sat","Sun"],
    palette="rocket",
    width=0.5,
    linewidth=2,
    showfliers=False,
    orient="h"
)

plt.title("Tips Distribution")
plt.grid(alpha=0.4)

plt.show()