def main():
    numb=[]
    x=0
    while x<12:
        RFIN=input('Enter Rainfall Amount: ')      
        if RFIN.strip()=="":
            print('Cannot Be Blank')
        else:
            try:
                number=float(RFIN)
                if number<0:
                    print('Cannot Be Negative')
                else:
                    numb.append(number)
                    x+=1
            except ValueError:
                print('Invalid Input')
    highest=max(numb)
    lowest=min(numb)
    total=sum(numb)
    ave=total/len(numb)
    print('Data:',numb)
    print('Highest Amount:', highest)
    print('Lowest Amount:', lowest)
    print('Total Rainfall:', total)
    print('Average:', ave)

main()
