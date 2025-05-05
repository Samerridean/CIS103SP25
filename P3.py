import math
def main():
    pounds=float(input('Enter Number of Pounds Purchased:'))
    if pounds<=0:
        print('Cannot be zero or negative')
    else:
        GS=pounds*.99
    if (pounds>=10) and (pounds<=99.99):
        DA=GS*.1
    elif (pounds>=100) and (pounds<=999.99):
        DA=GS*.2
    elif (pounds>=1000) and (pounds<=9999.99):
        DA=GS*.3
    elif pounds>=10000:
        DA=GS*.4
    FA=GS-DA
    print('Number of Pounds:',pounds)
    print('Gross Sales:',GS)
    print('Discount:',DA)
    print('Final Amount:',FA)
main()
