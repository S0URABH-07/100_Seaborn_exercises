# Histogram plot in seaborn and organized data using bins
# kde -> kernal density estimator
# rug -> add line on x-axis
# change color and convert figure into log
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

load_data = sns.load_dataset("penguins")
sns.displot(load_data["bill_length_mm"],kde=True , rug=True ,color="r",log_scale=True)
plt.show()