import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

bins = [18, 25, 35, 45, 55, 65]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65"
]

df["AgeGroup"] = pd.cut(df["Age"],bins=bins,labels=labels)

attrition_rate = (df.groupby("AgeGroup")["Attrition"].apply(lambda x: (x == "Yes").mean() * 100).reset_index(name="AttritionRate"))

print(attrition_rate)

plt.figure(figsize=(8,5))

sns.barplot(data=attrition_rate,x="AgeGroup",y="AttritionRate")

plt.title("Attrition Rate by Age Group")

plt.show()