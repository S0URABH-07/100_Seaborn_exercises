# Use seaborn and draw line plot using column name 
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=load_data)
print(load_data)
plt.show()