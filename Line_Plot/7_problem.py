# Use seaborn and draw line plot using column name and according to perticular column using hue=column_name and change style or color
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=load_data,hue="sex",style="sex",palette='spring')
plt.show()