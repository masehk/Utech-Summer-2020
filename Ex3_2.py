Year = int(input('Please Enter Year = '))
if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0):
    print('Its a leap year !')
else:
    print('Its NOT a leap year !')
