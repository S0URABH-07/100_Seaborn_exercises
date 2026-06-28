# Strip Plot on Top of a Box Plot
# The strip plot shows:
# Every individual observation
# This combination is widely used in reports and dashboards.

import matplotlib.pyplot as plt 
import seaborn as sns

load_data = sns.load_dataset("tips")
plt.figure(figsize=(10,6))

sns.boxplot(
    x="day",
    y="total_bill",
    data=load_data,
    color="lightgray"
)

sns.stripplot(
    x="day",
    y="total_bill",
    data=load_data,
    hue="time",
    dodge=True,
    jitter=True,
    alpha=0.8,
    size=6
)

plt.title("Box Plot + Strip Plot")

plt.show()