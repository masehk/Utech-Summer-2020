
""" 045 """
x = 0
while x < 51:
    y = int(input(' input number =  '))
    x += y
    print('The total is ',x)
print('The total is over 50')

""" 046 """
x = 0
while x <=5:
    x = int(input('Enter a number =  '))
print('The last number you entered was ',x)

""" 047 """
x = int(input('Insert a number =   '))
Answer = 'y'
while Answer == 'y':
    y = int(input('Another =   '))
    x += y
    Answer = input('Do you want add another ?  ')
print(x)

""" 048 """
count = 0
Ans = 'yes'
while Ans == 'yes':
    person = input('Name of the person ?   ')
    print(person + ' has now been invited')
    count += 1
    Ans = input('Do you still wanna invite ?  ').lower()
print(count)

""" 049 """
compnum = 50
x = int(input('Your first guess ?  '))
count = 1
while x != 50:
    if x > 50:
        print('Too high')
    if x < 50:
        print('Too low')
    count += 1
    x = int(input('Another guess ?  '))
print('Well done, you took ', count, ' attempts')

""" 050 """
x = int(input('A number between 10 and 20 =  '))
while x < 10 or x > 20:
    if x > 20:
        print('Too high')
    if x < 10:
        print('Too low')
    x = int(input('Try again =  '))
print('Thank you')

""" 051 """
num = 10
while num > 0:
    print('There are ', num, ' green bottles hanging on the wall, ', num, 'green bottles hanging on the wall, adn if 1 green bottle should accidentally fall')
    ans = int(input('How many green bottles will be hanging on the wall ?  '))
    while ans != num-1:
        ans = int(input('No, Try again =  '))
    num -= 1
print('There are no more green bottles hanging on the wall')



















