L_Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def Leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

Year = int(input('Please Enter Year = '))

Month = int(input('Please Enter Month = '))
if Month > 12:
    print('Month cannot be over 12')
    Month = int(input('Please Enter Month = '))
    
Day = int(input('Please Enter Day = '))
if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
    if Day > 31:
        print('Day cannot be over 31')
        Day = int(input('Please Enter Day = '))
if Month == 4 or Month == 6 or Month == 9 or Month == 11:
    if Day > 30:
        print('Day cannot be over 30')
        Day = int(input('Please Enter Day = '))
if Month == 2:
    if Leap(Year):
        if Day > 29:
            print('Day cannot be over 29')
            Day = int(input('Please Enter Day = '))
    else:
        if Day > 28:
            print('Day cannot be over 28')
            Day = int(input('Please Enter Day = '))

Count = sum(L_Months[:Month-1])
Count += Day
if Leap(Year):
    Count += 1

print(Count)
