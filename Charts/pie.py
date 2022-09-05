import matplotlib.pyplot as plt


finnish = 4822690
swedish = 287954
sami = 2004
other = 412664

size_of_groups=[finnish, swedish, sami, other]
labels =["finnish" , "swedish", "sami", "other"]

plt.pie(size_of_groups, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
plt.suptitle('Population according to language 2019')
plt.show()
