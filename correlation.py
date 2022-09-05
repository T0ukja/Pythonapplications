#pip install scipy
from scipy.stats.stats import pearsonr   
math = [1,4,5,5,2,3,4,5,3,3]
eng = [5,4,3,2,5,1,5,5,5,2,]   
print(pearsonr(math,eng))
