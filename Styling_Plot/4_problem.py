# Strip plot and Dashboard-Style Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(
    style="dark",
    context="poster"
)

plt.figure(figsize=(12,7))

sns.stripplot(
    x="day",
    y="tip",
    hue="sex",
    data=tips,
    jitter=True,
    dodge=True,
    alpha=0.7,
    size=7
)

plt.title("Dashboard Style Strip Plot", fontsize=20)

plt.xticks(rotation=20)

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.show()