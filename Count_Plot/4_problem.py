# Count plot with some diffrent parameters
# A count plot shows how many times each category appears in a dataset
import seaborn as sns
import matplotlib.pyplot as plt

load_data = sns.load_dataset("penguins")
sns.countplot(x="species", hue="island" ,order=["Chinstrap species","Adelie" ,"Gentoo"] ,hue_order=["Biscoe","Torgersen" ,"Dream"],data=load_data, saturation=0.3)

plt.show()