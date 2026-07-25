import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Department")
plt.title("Employees by Department")
plt.xticks(rotation=20)
plt.show()