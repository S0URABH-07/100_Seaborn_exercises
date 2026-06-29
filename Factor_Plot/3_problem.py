# Box plot using catplot 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.catplot(
    data=tips,
    x="day",
    y="tip",
    hue="smoker",
    kind="box",
    palette="viridis",
    height=6,
    aspect=1.5,
    linewidth=2,
    width=0.6
)

g.set_titles("Tips Distribution")

plt.show()