# Strip plot 
# Nearly Every Important Parameter Together

import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
plt.figure(figsize=(11,7))

sns.stripplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=load_data,
    palette="viridis",
    dodge=True,
    jitter=0.3,
    size=9,
    alpha=0.65,
    edgecolor="black",
    linewidth=1,
    order=["Thur","Fri","Sat","Sun"]
)

plt.title("Advanced Strip Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.grid(alpha=0.9)
plt.legend(title="Gender")

plt.show()