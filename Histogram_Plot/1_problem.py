# Histogram plot in seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins")
print(load_data)
sns.displot(load_data["bill_length_mm"])
plt.show()