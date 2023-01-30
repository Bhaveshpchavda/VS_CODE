from datetime import *
from time import *

print("username =")
un = str(input())
print("email-id =")
Em = str(input())
print("Age =")
a = int(input())

p_info = [un, Em, a]

if un and Em and a in p_info:
    print("Name of the user is =" , un)
    print("Mail-id of the user is =" , Em)
    print("Age of the user is =" , a)
    ND = date.today()
    T_day = ND.strftime('%d,%m,%Y')
    print("Last date of the edit :",T_day)

    N = datetime.now()
    T_Time = N.strftime("%H:%M:%S")
    print("The time of the last edit :",T_Time)
