year = int(input("Enter the year : "))
day = int(input("Enter the day as a number : "))
months = ['January', 'February', 'March', 'April', 'May', 'June',
'July','August', 'September', 'October', 'November', 'December']
month_days = [31,28,31,30,31,30,31,31,30,31,30]
Days = ['Sun','Mon','Tue','Wed','Thurs','Fri','Sat']
leap_year = year%4
if not leap_year:
    month_days[1] = month_days[1] + 1
day1 = day - 1
print(f"{months[0]} 1, {year} is {Days[day1]}day")
for i in range(0,11):
    day1 = day1 + month_days[i]
    print(f"{months[i+1]} 1, {year} is {Days[day1%7]}")
