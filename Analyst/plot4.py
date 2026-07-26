import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
sns.histplot(df["Age"], bins=15, kde=True)
plt.show()