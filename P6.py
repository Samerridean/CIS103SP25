answer='y'
while((answer=='y')or(answer=='Y')):
    MR=float(input('Enter Minutes: '))
    if MR<5:
        print('Cannot be Less than 5')
    else:
        CD=5
        while (CD<=MR):
            C=CD*4.33
            print('Minutes: ',CD,' Calories: ',C)
            CD=CD+5
    answer=input('Again? y/n: ')
print('-DONE-')
