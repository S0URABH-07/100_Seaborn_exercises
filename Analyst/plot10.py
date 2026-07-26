import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
salary = (df.groupby("JobRole")["MonthlyIncome"].mean().reset_index())

plt.figure(figsize=(12,5))

sns.barplot(data=salary,x="MonthlyIncome",y="JobRole")

plt.show()