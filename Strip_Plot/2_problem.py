# Strip plot 
# hue, palette, dodge, jitter, size

import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
plt.figure(figsize=(9,6))

sns.stripplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=load_data,
    palette="Set2",
    dodge=True,
    jitter=True,
    size=10
)

plt.title("Total Bill Distribution by Day and Gender")
plt.show()