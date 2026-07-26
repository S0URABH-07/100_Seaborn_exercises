import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))

sns.heatmap(corr,annot=True,cmap="coolwarm")

plt.show()