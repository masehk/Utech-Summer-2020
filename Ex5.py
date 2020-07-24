
""" 069 """
Tup_Coun = ('Iran', 'Germany', 'Canada', 'America', 'England' )
print(Tup_Coun)
User_Coun = input('Select One Of The Above =  ').lower().capitalize()
Index = Tup_Coun.index(User_Coun)
print(Index)

""" 070 """
Tup_Coun = ('Iran', 'Germany', 'Canada', 'America', 'England' )
print(Tup_Coun)
User_Coun = int(input('Select An INDEX Of The Above =  '))
print(Tup_Coun[User_Coun])

""" 071 """
L_Sport = ['Football', 'Basketball']
Fav_Sport = input('Whats your Fav Sport ?  ')
L_Sport.append(Fav_Sport)
L_Sport.sort()
print(L_Sport)

""" 072 """
Sch_Sub = ['Math', 'Biology', 'Physics', 'Geology', 'History', 'Science']
print(Sch_Sub)
Dislike = input('Which of the above you dont like ?   ').lower().capitalize()
Sch_Sub.remove(Dislike)
print(Sch_Sub)

""" 073 """
Food_1 = input('Your 1st fav food ?  ')
Food_2 = input('Your 2nd fav food ?  ')
Food_3 = input('Your 3rd fav food ?  ')
Food_4 = input('Your 4th fav food ?  ')

Dic_Food = {1:Food_1, 2:Food_2, 3:Food_3, 4:Food_4}
print(Dic_Food)

Del_Food = int(input('Which one to detele ?  '))
del Dic_Food[Del_Food]
print(Dic_Food)

""" 074 """
L_Color = ['Red', 'Blue', 'Yellow', 'Black', 'Brown', 'Purple', 'Gray', 'White', 'Orange', 'Navy']
start = int(input('Enter a start number between 0 and 4 =  '))
end = int(input('Enter an end number between 5 and 9 =   '))
print(L_Color[start:end+1])

""" 075 """
L_Num = [111, 222, 333, 444]
for i in L_Num:
    print(i)
Num = int(input('Enter a 3digit num =   '))
if Num in L_Num:
    print(L_Num.index(Num))
else:
    print('That is not on the list')
    
""" 076 """
People = []
People.append(input('Enter the 1st person   '))
People.append(input('Enter the 2nd person   '))
People.append(input('Enter the 3rd person   '))
x = input('Do You Want To Add ? ').lower()
while x== 'yes':
    People.append(input("Enter The Name : "))
    x = input("Do You Want To Add?   ").lower()
print(len(People))

""" 077 """
People = []
People.append(input('Enter the 1st person   '))
People.append(input('Enter the 2nd person   '))
People.append(input('Enter the 3rd person   '))
x = input('Do You Want To Add ? ').lower()
while x== 'yes':
    People.append(input("Enter The Name : "))
    x = input("Do You Want To Add?   ").lower()
print(People)
Person = input('Chose one   ')
print(People.index(Person))
Answer = input('Do you still want to invite him/her ?   ').lower()
if Answer == 'no':
    People.remove(Person)
print(People)

""" 078 """
L_Prog = ['Dorehami', 'Khandevane', '90', 'Barare']
for i in L_Prog:
    print(i)
New_Prog = input('Enter another program =   ')
New_Prog_Place = int(input('And where ?   '))
L_Prog.insert(New_Prog_Place, New_Prog)
print(L_Prog)

""" 079 """
nums = []
for i in range(3):
    nums.append(input('Enter a number =   '))
    print(nums)
if input('Keep the last ?  ').lower() == 'no':
    nums.remove(nums[-1])
    print(nums)





















