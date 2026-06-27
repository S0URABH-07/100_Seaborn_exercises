# Violin plot with smoother shape
# Small value → More detailed (wiggly) shape 
# Large value → Smoother shape

import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.violinplot(x="species", y="bill_length_mm",data=load_data, bw_method=1 )

plt.show()