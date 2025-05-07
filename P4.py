def main():
    Name=input('Enter First Name:')
    AN=input('Enter Account Number:')
    PA=input('Enter Payment Amount:')
    if Name.isspace():
        NE=' ERROR: Cannot Be Blank'
    elif Name.isnumeric():
        NE=' ERROR: Must be Alphabetic'
    elif len(Name)<3:
        NE=' ERROR: Cannot be Less than 3 Characters'
    else:
        NE=' '
    if AN.isspace():
        AE=' ERROR: Cannot Be Blank'
    elif AN.isalpha():
        AE=' ERROR: Must Be Numeric'
    elif len(AN)<9:
        AE=' ERROR: Must Be 9 Digits'
    else:
        AE=' '
    if PA.isspace():
        PE=' ERROR: Cannot Be Blank'
    elif PA<='0':
        PE=' ERROR: Cannot Be Zero or Negative'
    else:
        PE=' '
        
    print('Name:',Name,NE)
    print('Accounr Number:',AN,AE)
    print('Payment Amount:',PA,PE)
main()
