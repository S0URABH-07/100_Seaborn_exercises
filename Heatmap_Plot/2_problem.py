# Draw Heatmap plot with annot
# annot-> Shows the actual values inside each cell.
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

sns.heatmap(data, annot=True)
plt.show()