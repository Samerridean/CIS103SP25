# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n'*0)
    AssesmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = getinput('Enter value of property: ')
    LocalTaxRate = getinput('Enter loacal tax rate: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    print('\n'*1)
    AssessedValue= PropertyValue * AssesmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*1)
    print(' Property tax due: ',TotalPropertyTax)
    print('\n'*2)
    return
main()
#Tax Rate 7.149
