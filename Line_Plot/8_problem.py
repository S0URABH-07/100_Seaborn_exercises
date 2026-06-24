# Add marker 
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=load_data,hue="sex",style="sex",palette='spring' , markers=["o",">"])
plt.show()