import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
department = (
    df.groupby("Department")
      .agg(
          AttritionRate=(
              "Attrition",
              lambda x: (x == "Yes").mean() * 100
          ),
          OvertimeRate=(
              "OverTime",
              lambda x: (x == "Yes").mean() * 100
          )
      )
      .reset_index()
)
plot_data = department.melt(
    id_vars="Department",
    var_name="Metric",
    value_name="Percentage"
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=plot_data,
    x="Department",
    y="Percentage",
    hue="Metric"
)

plt.title("Department-wise Attrition vs Overtime")

plt.show()