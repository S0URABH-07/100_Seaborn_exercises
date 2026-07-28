import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
analysis = (df.groupby("PerformanceRating").agg(AverageSalaryHike=("PercentSalaryHike", "mean")).reset_index())
plt.figure(figsize=(8,5))

sns.lineplot(
    data=analysis,
    x="PerformanceRating",
    y="AverageSalaryHike",
    marker="o"
)

plt.title("Performance Rating vs Salary Hike")

plt.show()