import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
sns.barplot(data=df,x="Gender",y="MonthlyIncome")

plt.show()