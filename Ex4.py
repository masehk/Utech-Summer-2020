
""" 012 """
Num_1 = int(input('Enter first number = '))
Num_2 = int(input('Enter second number = '))
if Num_1 > Num_2:
    print(Num_2,Num_1)
else:
    print(Num_1,Num_2)
    
""" 013 """
Num = int(input('Enter a number below 20 = '))
if Num >= 20:
    print('Too high')
else:
    print('Thank you')
    
""" 014 """
Num = int(input('Enter a number between 10 and 20(inclusive) = '))
if Num <=20 and Num >= 10:
    print('Thank you')
else:
    print('Incorrent answer')
    
""" 015 """
Color = input('Whats your fav color ?   ')
Mine = 'red'
if Color == Mine or Color == Mine.upper() or Color == Mine.capitalize():
    print('I like red too')
else:
    print("I don't like " + Color + " ,I prefer red")
    
""" 016 """
rain = input('Is it raining ?  ').lower()
if rain == 'yes':
    wind = input('Is it Windy ?  ').lower()
    if wind == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
    
""" 017 """
Age = int(input('How old are you ?   '))
if Age >= 18:
    print('You can Vote')
elif Age == 17:
    print('You can learn to drive')
elif Age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-or-Treating')
    
""" 018 """
Num = int(input('Enter a number = '))
if Num < 10:
    print('Too low')
elif Num > 20:
    print('Too high')
else:
    print('Correct')
    
""" 019 """
Num = int(input('Enter 1,2 or 3    '))
if Num == 1:
    print('Thank you')
elif Num ==2:
    print('Well Done')
elif Num == 3:
    print('Correct')
else:
    print('Error Message')
























