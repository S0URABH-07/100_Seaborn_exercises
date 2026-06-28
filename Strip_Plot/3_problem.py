# Strip plot 
# order, linewidth, edgecolor, palette, jitter

import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
plt.figure(figsize=(10,6))

sns.stripplot(
    x="day",
    y="tip",
    hue="sex",
    data=load_data,
    order=["Thur","Fri","Sat","Sun"],
    jitter=0.35,
    palette="deep",
    size=9,
    linewidth=1.2,
    edgecolor="black"
)

plt.title("Tips by Day")
plt.grid(alpha=0.3)

plt.show()