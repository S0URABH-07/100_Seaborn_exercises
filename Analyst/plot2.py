import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Department",
    y="MonthlyIncome",
    estimator="mean"
)
plt.xticks(rotation=20)
plt.show()