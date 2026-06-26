# Heatmap using Numpy
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
mask = np.array([
    [False, True, False],
    [False, False, True],
    [True, False, False]
])

sns.heatmap(
    data,
    mask=mask,
    annot=True
)
plt.show()