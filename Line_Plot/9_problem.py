# Add dashes and remove legend
# Use head and tail for work on small data
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins").head(50)

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=load_data,hue="sex",style="sex",palette='spring' , markers=["o",">"] , dashes=False , legend=False)
plt.show()