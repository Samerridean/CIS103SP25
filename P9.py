ans='y'
while (ans=='y' or ans =='Y'):
    def getnum(N):
        numb=float(input(N))
        return numb
    def AtH():
        try:
            A=getnum('Enter Acres:')
            H=A*0.4047
            if H<=-1:
                print('Input Error - Acres')
            else:
                print('Hectares:',H)
        except:
            print('Input Error - Acres')
    def QtL():
        try:
            Q=getnum('Enter Quarts:')
            L=Q*0.946353
            if L<=-1:
                print('Input Error - Quarts')
            else:
                print('Liters:',L)
        except:
            print('Input Error - Quarts')
    def FtK():
        try:
            F=getnum('Enter Fahrenheit:')
            K=(F-32)*(5/9)+273.15
            print('Kelvin:',K)
        except:
            print('Input Error - Fahrenheit')
    def main():
        AtH()
        QtL()
        FtK()
    main()
    ans=input('Again? y/n: ')
