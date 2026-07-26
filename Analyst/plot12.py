import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

plt.figure(figsize=(12,6))

departments = df["Department"].unique()

salary = [df[df["Department"] == d]["MonthlyIncome"] for d in departments]

sns.boxplot(
    data=df,
    x="Department",
    y="MonthlyIncome",
    hue="Attrition"
)

plt.xticks(rotation=20)

plt.title("Department-wise Salary Distribution by Attrition")

plt.show()