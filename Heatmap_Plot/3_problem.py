# Draw Heatmap plot with color change USE-> cmap
# annot-> Shows the actual values inside each cell. in float
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

sns.heatmap(data, annot=True ,fmt=".1f" , cmap="viridis")
plt.show()