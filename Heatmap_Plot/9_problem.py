# Heatmap using Pandas Dataframe
# Rows and columns are labeled automatically
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Math": [90, 80, 70],
    "Science": [85, 60, 95],
    "English": [88, 75, 91]
}, index=["Alice", "Bob", "Charlie"])

sns.heatmap(df,annot=True)
plt.show()