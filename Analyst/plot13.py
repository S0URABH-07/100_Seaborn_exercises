import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

analysis = (
    df.groupby("JobRole").agg(
          AverageSalary=("MonthlyIncome", "mean"),
          AverageSatisfaction=("JobSatisfaction", "mean")
      ).sort_values("AverageSalary", ascending=False)
)

print(analysis)
plt.figure(figsize=(12,6))

sns.scatterplot(
    data=analysis,
    x="AverageSalary",
    y="AverageSatisfaction",
    s=120
)

for role in analysis.index:
    plt.text(
        analysis.loc[role, "AverageSalary"],
        analysis.loc[role, "AverageSatisfaction"],
        role,
        fontsize=8
    )

plt.title("Salary vs Job Satisfaction by Job Role")

plt.show()