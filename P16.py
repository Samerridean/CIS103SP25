import math
def sum(a):
    if a<=1:
        return a
    else:
        return a+sum(a-1)
def main():
    ans='y'
    while ans=='y':
        number=input('Enter a positive Number:')
        if number == "":
            print('Cannot be blank')
        elif number < '0':
            print ('Cannot be Negative')
        elif number.isalpha():
            print('Must be a Number')
        else:
            RN=int(number)
            print(sum(RN))
        ans=input('Again? y/n:')
main()
