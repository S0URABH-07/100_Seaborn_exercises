import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
sns.boxplot(data=df,x="Department",y="MonthlyIncome")

plt.xticks(rotation=20)

plt.show()