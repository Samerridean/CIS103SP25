print('Table Codes: A=Add, S=Subtract, M=Multiply, D=Divide')
TC=input('Enter Table Code:')
N=float(input('Enter Number for Table:'))
#Addition
if (TC=='A'):
    for A in range(1,11,1):
     print(A+N,'=',N,'+',A)
#Subtraction
elif (TC=='S'):
    for S in range(1,11,1):
        print(S-N,'=',N,'-',S)
#Multiplication
elif (TC=='M'):
    for M in range(1,11,1):
        print(M*N,'=',N,'*',M)
#Division
elif (TC=='D'):
    for D in range(1,11,1):
        print(D/N,'=',N,'/',D)
else:
    print('Must Use Table Code')
