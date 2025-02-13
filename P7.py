#Miles To Kilometers
def MtK(M):
    K=M*1.609344
    return K
def main():
    M=float(input('Enter Miles:'))
    Cal=MtK(M)
    print('Kilometers:',Cal)
main()
#Fahrenheit to Clesius
def FtC(F):
    C=(F-32)*5/9
    return C
def main():
    F=float(input('Enter Fahrenheit:'))
    CalC=FtC(F)
    print('Celsius:',CalC)
main()
#Pounds To Kilograms
def PtK(P):
    Kilo=P*0.45359237
    return Kilo
def main():
    P=float(input('Enter Pounds:'))
    CalK=PtK(P)
    print('Kilograms:',CalK)
main()
#Can be condensed into four functions
