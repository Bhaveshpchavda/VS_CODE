# print("Hello World")
# print(5//2)

# first = int(input("Enter First number : "))
# opretor = input("Enter Opretor (+,-,/,*,%): ")
# second = int(input("Enter Second Number: "))

# if(opretor=="+"):
#     print(first,opretor,second,"=",first+second)

# if(opretor=="-"):
#     print(first,opretor,second,"=",first-second)

# if(opretor=="/"):
#     print(first,opretor,second,"=",first/second)

# if(opretor=="*"):
#     print(first,opretor,second,"=",first*second)

# if(opretor=="%"):
#     print(first,opretor,second,"=",first%second)

# for i in range(10000):
#     print(i)

# i=1
# while i<5:
#     print(i)
#     i += 1

##################### NumPy #####################

import numpy as np
# print("hello world")

# listarr=np.array([[3,2,4],[2,6,5],[9,8,7]])
# print(listarr)

# arr=np.array({21,34,32})
# print(type(arr))

# zeros = np.zeros((2,3))
# rng=np.arange(99)
# # lp=np.linspace(1,50,10)
# # print(zeros)
# print(rng)

a= np.array(['ICT','Gnu','Ahmedabad'])
# print(type(a)) 
# print(a) 
b=np.arange(0,10,2)
c=np.zeros((3,3))
c=np.zeros(3)
e=np.eye(5)
arr1=np.random.randint(1,100,25)
arr2=arr1.reshape(5,5)
# print(arr1)
# print(arr2)
l = [1,5,3,8,2,3,6,7,5,2,9,11,2,5,3,4,8,9,3,1,9,3] 
a = np.array(l)
# print('Min way1 = ',a.min())
# print('Min way2 = ',np.min(a))
# print(a.max())
# print('Max way1 = ',a.max())
# print('Max way2 = ',np.max(a))
array2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
# print('sum (cols)= ',array2d.sum(axis=0)) #Vertical
# print('sum (rows)= ',array2d.sum(axis=1)) #Horizontal
arr = np.array([['a','b','c'],['d','e','f'],['g','h','i']]) 
# print(arr)
# print('double = ',arr[2][1]) # double bracket notaion
# print('single = ',arr[2,1]) # single bracket notation
arr = np.array(['a','b','c','d','e','f','g','h']) 
# print(arr[2:5]) 
# print(arr[:5]) 
# print(arr[5:]) 
# print(arr[2:7:2]) 
# print(arr[::-1])
arr = np.array([['a','b','c'],['d','e','f'],['g','h','i']]) 
# print(arr)
# print(arr[0:2 , 0:2]) #first two rows and cols
# print(arr[::-1]) #reversed rows
# print(arr[: , ::-1]) #reversed cols
# print(arr[::-1,::-1]) #complete reverse
dt = np.dtype([('name', 'S10'),('age', int)]) 
arr2 = np.array([('ICT',200),('ABC',300),('XYZ',100)],dtype=dt) 
arr2.sort(order='name') 
# print(arr2)

print()

