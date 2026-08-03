import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

salary_std = (df.groupby("Department").agg(AverageSalary=("MonthlyIncome", "mean"),SalaryVariation=("MonthlyIncome", "std")).sort_values("SalaryVariation", ascending=False))
plt.figure(figsize=(8,5))

sns.barplot(
    data=salary_std.reset_index(),
    x="Department",
    y="SalaryVariation"
)

plt.title("Salary Variation by Department")

plt.show()