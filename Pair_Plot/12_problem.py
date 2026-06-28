# Pair plot with diffrent parameteres
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(
    iris,
    hue="species",
    palette="PuBu",
    diag_kind="kde",
    kind="kde",
    height=2.5,
    aspect=1,
)

plt.show()