import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
analysis = df[
    [
        "TotalWorkingYears",
        "MonthlyIncome",
        "Attrition"
    ]
]
left = analysis[analysis["Attrition"] == "Yes"]

stay = analysis[analysis["Attrition"] == "No"]
plt.figure(figsize=(10,6))

sns.scatterplot(data=df,x="TotalWorkingYears", y="MonthlyIncome", hue="Attrition", style="Attrition", s=80)

plt.title("Experience vs Salary by Attrition")

plt.show()