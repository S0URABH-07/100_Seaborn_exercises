# Count plot with all parameters
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(
    x="island",
    hue="sex",
    palette="Set2",
    saturation=0.8,
    width=0.7,
    dodge=True,
    stat="count",
    data=load_data
)

plt.title("Count Plot Example")
plt.xlabel("Day")
plt.ylabel("Number of Customers")
plt.show()