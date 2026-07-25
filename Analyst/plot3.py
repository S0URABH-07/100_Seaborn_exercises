import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyIncome"], bins=20, kde=True)
plt.show()