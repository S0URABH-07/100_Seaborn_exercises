import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
analysis = (
    df.groupby("JobSatisfaction").agg(
          AttritionRate=(
              "Attrition",
              lambda x: (x == "Yes").mean() * 100
          )
      ).reset_index()
)
plt.figure(figsize=(8,5))

sns.lineplot(
    data=analysis,
    x="JobSatisfaction",
    y="AttritionRate",
    marker="o"
)

plt.title("Job Satisfaction vs Attrition")

plt.show()