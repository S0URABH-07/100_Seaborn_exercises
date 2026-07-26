import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
sns.scatterplot(data=df,x="TotalWorkingYears",y="MonthlyIncome")
plt.show()