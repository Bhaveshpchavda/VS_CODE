import numpy as np 
import matplotlib.pyplot as plt

x = np.array([20, 18, 30, 22, 15]) 
y = np.arange(1, 6) 
z = np.array([19, 22, 33, 30, 19]) 

plt.title("Results")
plt.xlabel("Total Subjects")
plt.ylabel("Total Marks") 

# plot bars for x and z 
plt.bar(y-0.2, x, width=0.4, color='green', align='center') 
plt.bar(y+0.2, z, width=0.4, color='red', align='center') 

plt.xticks(y, ('PNS', 'OS', 'FET', 'PYTHON', 'SE'))
plt.show()
