import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
overtime = (df.groupby("JobRole").agg(OvertimeRate=("OverTime",lambda x: (x == "Yes").mean() * 100)).sort_values("OvertimeRate",ascending=False).reset_index())
plt.figure(figsize=(12,6))

sns.barplot(
    data=overtime,
    x="OvertimeRate",
    y="JobRole"
)

plt.title("Overtime Rate by Job Role")

plt.show()