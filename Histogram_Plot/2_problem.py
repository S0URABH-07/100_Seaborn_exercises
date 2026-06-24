# Histogram plot in seaborn and organized data using bins
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins")
print(load_data)
sns.displot(load_data["bill_length_mm"],bins=[35,40,45,50,55,65])
plt.show()