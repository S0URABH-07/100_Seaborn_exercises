# Draw Heatmap plot with min or max value
# vmin or vmax -> Manually control the color scale 
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

sns.heatmap(data,vmin=0 , vmax=100)
plt.show()