import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

salary = (df.groupby(["Department", "EducationField"])["MonthlyIncome"].mean().reset_index())

plt.figure(figsize=(12,6))

sns.barplot(
    data=salary,
    x="Department",
    y="MonthlyIncome",
    hue="EducationField"
)

plt.xticks(rotation=20)

plt.title("Average Salary by Department and Education Field")

plt.show()