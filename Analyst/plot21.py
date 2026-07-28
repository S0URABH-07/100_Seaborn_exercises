import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
travel = (
    df.groupby("BusinessTravel").agg(
          AttritionRate=(
              "Attrition",
              lambda x: (x == "Yes").mean() * 100
          )
      ).reset_index()
)
plt.figure(figsize=(8,5))

sns.barplot(
    data=travel,
    x="BusinessTravel",
    y="AttritionRate"
)

plt.title("Attrition Rate by Business Travel")

plt.show()