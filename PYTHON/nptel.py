         ###########################------ NPTEL ------###########################

# a=1
# print(a)
# a=a+1
# print(a)

# n=input("What is Your name ?")
# print("Hello",n,"!")

# a = int(input("Enter Amount: "))
# ans=a*.9
# print(ans)

######### If StateMents ##########

# a=int(input("Enter The Choice :"))
# if(a==1):
#     print("You Enter one")
# elif(a==2):
#     print("you Entered two.")
# else:
#     print("Invalid !")

############ Loops ###########

# for i in range(10):
#     print(i)
#     print(i+1)

# ans=0
# for i in range(10001):
#     ans=ans+i
# print("First",i,"numbers,when added, gives",ans)

# t=int(input("Which table you want ? \n"))
# print("Table of ",t,"is :")
# for i in range(11):
#     print(t,"X",i,"=",t*i)

# print("Hello World , we are starting...")
# n=1; c=1 
# while(c==1):
#     print("\nToken No.",n,"may come in" )
#     c=int(input("Continue(0/1) ? \n"))
#     n=n+1
# print("Thank You, See you Tomorrow..")

############# Lists && Slicing ##############

# shopping=["Bread","Coffee","Mug","Jam"]
# # print(shopping)
# shopping.append("Cornflex")
# shopping.insert(5,"Maggie")
# for item in shopping:
#     print(item)

# print(shopping)
# print(shopping.count("Mug"))
# print(shopping.pop())
# print(len(shopping))
# shopping.reverse()
# print(shopping)

# age = [1,33,54,86,3,34,34,34,54,6,5,76,56,86,23,44,67,23,12,19]
# # print(age.count(34))
# # print(len(age))
# age.sort()
# age.reverse()
# print(age)

# students=['Bhavesh','Vimal','Yogesh','Daxil','Akshit','Preet']
# students.insert(0,"SSGK")
# # print(students[0])
# print(students[1:4])
# print(students[1:])
# print(students[1::2]) ## last one is for interval it's like if i wanţinterval of 2 i'll write 3
# print(students[::-1]) ## reverse

############# FizzBuzz ###########
# def FizzBuzz(r):
#     for i in range(1,r):
#         if(i%3==0 and i%5==0):
#             print(str(i)+"--> FizzBuzz")
#         elif(i%3==0):
#             print(str(i)+"--> Fizz")
#         elif(i%5==0):
#             print(str(i)+"--> Buzz")
#         else:
#             print(i)

# FizzBuzz(100)

# import matplotlib.pyplot as plt 
# plt.plot([1,5,9,23],[23,34,43,63],'ro')
# plt.xlabel("X")
# plt.ylabel("Y")

#################### Jumbled Word  ####################
# import random
# def choose():
#     word=['rainbow','computer','science','program','water','reverse','table','brownie','temple']
#     pick=random.choice(word)
#     return pick

# def jumble(word):
#     jumbled="".join(random.sample(word,len(word)))
#     return jumbled

# def thank(p1n,p2n,p1,p2):
#     print(p1n,' Your Score is :',p1)
#     print(p2n,' Your Score is :',p2)
#     print('Thanks For Play') 

# def play():
#     p1name=input("Player1, Enter Your name:")
#     p2name=input("Player2, Enter Your name:")
#     pp1=0
#     pp2=0
#     turn=0
#     while(1):
#         #Computer's Task
#         pickd_word=choose()
#         qn=jumble(pickd_word)
#         print(qn)
#         #Player 1 : 
#         if turn%2==0:
#             print(p1name,"Your turn")
#             ans=input("what is on my mind ?")
#             if ans==pickd_word:
#                 pp1=pp1+1
#                 print("Your Score is ",pp1)
#             else:
#                 print("Better Luck next Time...")
#             c=int(input("Continue(0/1)? "))
#             if c==0:
#                 thank(p1name,p2name,pp1,pp2)
#                 break

#         #Player 2 : 
#         else:
#             print(p2name,"Your turn")
#             ans=input("what is on my mind ?")
#             if ans==pickd_word:
#                 pp2=pp2+1
#                 print("Your Score is ",pp2)
#             else:
#                 print("Wrong Answer...")
#             c=int(input("Continue(0/1)? "))
#             if c==0:
#                 thank(p1name,p2name,pp1,pp2)
#                 break
#         turn=turn+1

# play()


################ File Handling ################

# with open("PYTHON\iofile.txt",'r+') as myfile:
#     print(myfile.read())
#     myfile.write("\n I'm Bhavesh Chavda")
# myfile.close()

# import random 

# def evolve(x):
#     ind=random.randint(0,len(x)-1)
#     p=random.randint(1,100)
#     # print(p)
#     if(p==1):
#         if(x[ind]=='0'):
#             x[ind]='1'
#         else:
#             x[ind]='0'

# with open("PYTHON\iofile.txt") as file:
#     x=file.read()
#     x=list(x)
# for i in range(0,1000):
#     evolve(x)
# print(x)

############### Magic Square #############
# def magic_square(n):
#     if n % 2 == 0:
#         print("n must be odd")
#         return

#     magicSquare=[]
#     for i in range(n):
#         l=[]
#         for j in range(n):
#             l.append(0)
#         magicSquare.append(l)

#     i=n//2
#     j=n-1

#     num=n*n
#     count=1
#     while(count<=num):
#         if(i==-1 and j ==n):
#             j=n-2
#             i=0
#         else:
#             if(j==n):
#                 j=0
#             if(i<0):
#                 i=n-1
#         if(magicSquare[i][j]!=0):
#             j=j-2
#             i=i+1
#             continue
#         else:
#             magicSquare[i][j] = count
#             count+=1    
#         i = i-1
#         j = j+1

#     for i in range(n):
#         for j in range(n):
#             print(magicSquare[i][j],end=' ')
#         print()

# magic_square(4)

########### Dobble Game - Spot the similarity #############
# import random
# import string
# symbols = []
# symbols = list(string.ascii_letters)
# # print(symbols)
# card1=[0]*5
# card2=[5]*5
# pos1=random.randint(0,4)
# pos2=random.randint(0,4)
# # print(pos1)
# # print(pos2)
# sameSymbols=random.choice(symbols)
# symbols.remove(sameSymbols)
# if(pos1==pos2):
#     card2[pos1]=sameSymbols
#     card1[pos1]=sameSymbols
# else:
#     card1[pos1]=sameSymbols
#     card2[pos2]=sameSymbols
#     card1[pos2]=random.choice(symbols)
#     symbols.remove(card1[pos2])
#     card2[pos1]=random.choice(symbols)
#     symbols.remove(card2[pos1])
# i=0
# while(i<5):
#     if(i!=pos1 and i!=pos2):
#         alphabet1=random.choice(symbols)
#         symbols.remove(alphabet1)
#         alphabet2=random.choice(symbols)
#         symbols.remove(alphabet2)
#         card1[i]=alphabet1
#         card2[i]=alphabet2
#     i=i+1
# print(card1)
# print(card2)
# ch=input("Spot the similar Symbol\n")
# if(ch==sameSymbols):
#     print("Right")
# else:
#     print("Wrong")

# import random  
# year = random.randint(1993,2018)
# print(year)
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("It's lap Year.")
# else:
#     print("not Leap Year.")

############### BirthDay Paradox ############
# import random,datetime
# birthday =[]
# i=0
# while(i<50):
#     year = random.randint(1950,2023)
#     #oldest person lived here is 73 years old
#     if(year%4==0 and year%100!=0 or year%400==0):
#         leap=1
#     else:
#         leap=0
#     month=random.randint(1,12)
#     if(month==2 and leap==1):
#         day =random.randint(1,29)
#     elif(month==2 and leap==0):
#         day = random.randint(1,28)
#     elif(month==7 or month==8):
#         day=random.randint(1,31)
#     elif(month%2!=0 and month<7):
#         day=random.randint(1,31)
#     elif(month%2==0 and month>7 and month<12):
#         day=random.randint(1,31)
#     else:
#         day=random.randint(1,30)
#     dd=datetime.date(year,month,day)
#     DayOfYear=dd.timetuple().tm_yday
#     i+=1
#     birthday.append(DayOfYear)

# birthday.sort()
# i=0
# while(i<50):
#     print(birthday[i])
#     i+=1

################# Guess the Movie ##############
# import random
# movies=['matrix','moon knight','gotham','boss baby','john wick','inception','jack ryan','the batman','the boys']
# def create_question(movie):
#     n=len(movie)
#     letters=list(movie)
#     temp=[]
#     for i in range(n):
#         if letters[i]==' ':
#             temp.append(' ')
#         else:
#             temp.append('_')
#     qn=''.join(str(x) for x in temp)
#     return qn

# def isPresent(letter,movie):
#     c=movie.count(letter)
#     if c==0:
#         return False
#     else:
#         return True
    
# def unlock(qn,movie,letter):
#     ref=list(movie)
#     qn_list=list(qn)
#     temp=[]
#     n=len(movie)
#     for i in range( n):
#         if ref[i]==' ' or ref[i]==letter:
#             temp.append(ref[i])
#         else:
#             if qn_list[i]=='_':
#                 temp.append('_')
#             else:
#                 temp.append(ref[i])
#     qn_new=''.join(str(x) for x in temp)
#     return qn_new


# def play():
#     p1name=input('Player1,Enter Your name: ')
#     p2name=input('Player2,Enter Your name: ')
#     pp1=0
#     pp2=0
#     turn=0
#     willing=True
#     while willing:
#         if turn%2==0:
#             #player1 turn
#             print(p1name,'Your turn ')
#             picked_movie=random.choice(movies)
#             qn=create_question(picked_movie)
#             print(qn)    
#             modified_qn=qn

#             not_said=True
#             while not_said:
#                 letter=input('Your letter: ')
#                 if(isPresent(letter,picked_movie)):
#                     #unlock
#                     modified_qn=unlock(modified_qn,picked_movie,letter)
#                     print(modified_qn)
#                     while True:
#                         try:
#                             d=int(input('Press 1 to guess , Press 2 for unlock new char: '))
#                             break
#                         except ValueError:
#                             print("Invalid input! Please enter an integer.")

#                     if d==1:
#                         ans=input('Your Ans: ')
#                         if ans==picked_movie:
#                             pp1+=1
#                             print('Correct')
#                             not_said=False
#                             print(p1name,'Your Score: ',pp1)
#                         else:
#                             print('Wrong ans.Try Again')

#                 else:
#                     print(letter,' not Found ')
#             while True:
#                 try:
#                     c=int(input('Continue?(0/1): '))
#                     break
#                 except ValueError:
#                     print("Invalid input! Please enter an integer.")
#             if c==0:
#                 print(p1name,' Your Score: ',pp1)
#                 print(p2name,' Your Score: ',pp2)
#                 print('Thanks For Playing')
#                 willing=False

#         else:
#             #player2 turn
#             print(p2name,'Your turn ')
#             picked_movie=random.choice(movies)
#             qn=create_question(picked_movie)
#             print(qn)    
#             modified_qn=qn

#             not_said=True
#             while not_said:
#                 letter=input('Your letter: ')
#                 if(isPresent(letter,picked_movie)):
#                     #unlock
#                     modified_qn=unlock(modified_qn,picked_movie,letter)
#                     print(modified_qn)
#                     while True:
#                         try:
#                             d=int(input('Press 1 to guess , Press 2 for unlock new char: '))
#                             break
#                         except ValueError:
#                             print("Invalid input! Please enter an integer.")
#                     if d==1:
#                         ans=input('Your Ans: ')
#                         if ans==picked_movie:
#                             pp2+=1
#                             print('Correct')
#                             not_said=False
#                             print(p2name,'Your Score: ',pp2)
#                         else:
#                             print('Wrong ans.Try Again')

#                 else:
#                     print(letter,' not Found ')
#             while True:
#                 try:
#                     c=int(input('Continue?(0/1): '))
#                     break
#                 except ValueError:
#                     print("Invalid input! Please enter an integer.")
#             if c==0:
#                 print(p1name,' Your Score: ',pp1)
#                 print(p2name,' Your Score: ',pp2)
#                 print('Thanks For Playing')
#                 willing=False
#         turn+=1

# play()

