import numpy as np
plant = np.arange(1, 9, 1) 
print("Total Plants : ", plant) 
y1 = plant.reshape(4, 2) 
print(y1) 
print("\nTwo Plants Died : ") 
y2 = y1[:3] 
print(y2) 
print("\nTwo Plants Of Same Types Are Added : ") 
y3 = np.insert(y2, 3, 3)
y4 = np.insert(y3, 3, 3) 
print(y4) 
print("\nResharping The Plants : ") 
y5 = y4.reshape(4, 2)
print(y5) 
print("\nPlant Died Due To Poor Nutrition : ") 

y6 = y5[1:] 
print(y6) 
print("\nSame Plants On Same Side : ") 
y7 = y6.reshape(2, 3)
y8 = np.sort(y7) 
print(y8) 
print("\n")
