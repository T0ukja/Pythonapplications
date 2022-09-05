
	
import pandas as pd
import matplotlib.pyplot as plt
var = pd.read_excel("pop.xlsx")
x = list(var['Years'])
y = list(var['Population'])
plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker=".",s=100,edgecolors="black",c="red")
plt.title("Finland human population 1200-2000")
plt.show()
