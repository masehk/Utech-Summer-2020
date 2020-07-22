Year = int(input('Enter Year = '))
if Year % 400 == 0:
    print('Its a leap year !')
elif Year % 100 == 0:
    print('Its NOT a leap year !')
elif Year % 4 == 0:
    print('Its a leap year !')
else:
    print('Its NOT a leap year !')
