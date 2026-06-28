# Strip plot 
# orient, hue, dodge, jitter, size

import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
plt.figure(figsize=(10,6))

sns.stripplot(
    y="day",
    x="total_bill",
    hue="smoker",
    data=load_data,
    orient="h",
    dodge=True,
    jitter=0.25,
    palette="deep",
    size=7
)

plt.title("Total Bill by Day (Smoker vs Non-Smoker)")

plt.show()