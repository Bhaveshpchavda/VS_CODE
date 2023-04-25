# with open('sample.txt','w') as f:
#     data = f.write("Hello world ")
 
# open('sample.txt','r')
# font = f.read()
 
#  class Train:
#     def __ticket__():
#         t=input("Enter category")
#         n=input("Amount oƒ tickets")
#         print(f"You boooked {n} seats in {t}")

#         def getfare():
#             print(f"Enter fare ")



# import random 
# r = random.randint(1,20)

# while(True):
#     inp=int(input())
#     if(inp<r):
#         print("Enter a greter number")
#     elif(inp>r):
#         print("Enter lesser number")
#     else:
#         print("Congrats you gaussed correct number...")
#         break; 


# def myfunc():
#     print("helllo world")

# def sum(a,b):
#     return a+b

# bhavesh= 93 

# myfunc() 
# print(bhavesh)
# result = sum(93,8)
# print(result)

# for x in range(10):
#     print(myfunc())

# l= []
# n = 5 
# for i in range(n):
#     a=int(input())
#     l.append(a)

# print(l)
# a=int(input())
# b=int(input())
# def func(a,b):
#     c=a*b
#     print(c)
# func(a,b)

#------->> Sequnce Packing
# def return_first_last_mid(name):
#     return name[0], name[1:-1] , name[-1]

# f,m,l = return_first_last_mid('alexzender')
# print('First:',f)
# print('mid:',m)
# print('Last:',l)

# evens=[2,4,6,8]
# f,*m,=evens
# print(f,m)

# class student():
#     def __init__(self,aname,amarks):
#         self.name=aname
#         self.marks=amarks

#     def printdetail(self,):
#         return f"Name is {self.name}.mark is {self.marks}"
#     pass

# f = open('iofile.txt','r')
# text = f.read()
# print(text)
# f.close()

# for k in range(1,25,3):
#  print(k)
# M='University'
# print(M[:-1])
# print(type({}))
# List=[6,1,2,3,8]
# print(List.extend([11,4,3,5]))
# print(List.pop(1))
# print(List)
# t=(1,2,3,4,3,8,9) 
# for i in range(0,len(t),2):
#     print(i)


# bhavesh = student()
# vimal=student()
# bhavesh.marks=56
# bhavesh.name="bhavesh"
# vimal.marks=34
# vimal.name="vimal"
# vimal = student("Bhavesh",25)
# print(vimal.marks)

# a = "I am Bhavesh"
# b= "Bhavesh"

# c= a.rfind('h')
# print(c)

# d= a.find('h')
# print(d)

# x='hell'
# print(x)
# print(type(x))
# n=123.82341 
# print(n)   
# type(n) 

# List
# list = ['bhavesh','vimal','akshit',101,123.12]
# print(type(list))
# temp = list.pop()
# print(temp)
# print(list)
# list.remove('bhavesh')
# list.clear()
# p=list.count('vimal')
# print(p)
#  list = ['ICT', 'Guni', 'Ahmedabad', 'ICT', 'Gujarat']
# list.reverse()
# print(list)
# y=list.sort()
# y=list
# print(list)
# y=list.sort(reverse=True)
# print(list)
# list = [1,2,3,4,5,4,5,6]
# print(list)
# list[6]='bhavesh'
# print(list)
# mylist=[9,8,7,list]
# print(mylist)
# print(len(list))
# print(len(mylist))
# print(mylist[2])

# Tupple
# tuple=(1,2,3,4,5,6)
# print(type(tupple))
# print(tuple[5])
# r=tuple[2:-2]
# print(r)
# print(tuple+tuple)
# print(tuple[-3])
# my_tuple=(12,23,34,tuple)
# print(my_tuple)
# print(len(my_tuple))
# print(my_tuple[3])
# t3 = (1567, 2876, -0.34, 'apple', (1,2,3), [4,5,6])
# print(t3)
# print(t3[-1][-3])

# Dictionary 
# d1 = {'brand':"Ford", 'modal':"Mustang", 'year':1970}
# print(type(d1))
# print(d1['modal'])
# d1['engine']='720HP'
# d1['Yugam'] = 10023
# # print(d1)
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# brands = ['ford', 'honda', 'toyota']
# modals = ['figo', 'accord', 'prius']
# years = [1960, 1970, 1980, 1990, 2000, 2010, 2022]
# engine = 'gasoline'
# features = []
# cardict = {'brand':brands, 'modal':modals, 'year':years,'engine':engine, 'feature':features}
# print(cardict)
# print(cardict.keys())
# print(type(cardict['feature']))
# print(cardict.get('brand'))

#  Sets
# myset = {1,2,6,4,5,1,2,3,6,7,8,9,9,9,9,9,9,9,9,9,9}
# print(type(myset))
# myset1= set()
# myset1.add(2)
# myset1.add(3)
# myset1.add(4)
# myset1.add(5)
# myset1.add(6)
# myset1.add((9,8,7))
# print(myset1)
# myset1.remove(5)
# print(myset1)
# set2 = {1,2,3,'ict',(7,8)}
# print(set2)

# Variable Declaration


# red_marbles = int(input())
# green_marbles = int(input())

# # Find the smaller value between red_marbles and green_marbles
# min_marbles = print(min(red_marbles, green_marbles))


# import numpy as np
# import pandas as pd
# i = ['name','address','phone','email','website']
# d = ['ICT', 'ahm',123, 'trk01@gnu.ac.in', 'ict.gnu.ac.in']

# s = pd.Series(data=d,index=i)
# print(s)



# import matplotlib.pyplot as plt
# # Data
# labels = ['A', 'B', 'C', 'D'] # Labels for each pie slice
# sizes = [15, 30, 45, 10] # Values for each pie slice
# colors = ['r', 'g', 'b', 'y'] # Colors for each pie slice
# # Plotting the pie chart
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
# # Adding a title
# plt.title('Pie Chart Example')
# # Display the chart
# plt.show()

# import matplotlib.pyplot as plt
# values1 = [5,8,9,4,1,6,7,2,3,8]
# values2 = [8,3,2,7,6,1,4,9,8,5]
# plt.plot(range(1,11),values1,c='r',lw=1,ls='--',marker='>')
# plt.plot(range(1,11),values2,c='b',lw=2,ls=':',marker='o')
# plt.show()

import matplotlib.pyplot as plt 
