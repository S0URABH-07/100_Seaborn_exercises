# Heatmap 
# Most Common Real-World Use: Correlation Matrix
# A correlation heatmap helps you see which variables are positively or negatively related.
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
corr = tips.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=2,
    linecolor="black",
    square=True,
    cbar=True
)

plt.title("Correlation Heatmap")

plt.show()