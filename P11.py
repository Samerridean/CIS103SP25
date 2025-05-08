from datetime import*
from time import*
def grades(points):
    if 900 <=points <=1000:
        return'A'
    elif 800<= points <=899:
        return'B'
    elif 700<= points <=799:
        return'C'
    elif 600<= points <=699:
        return'D'
    else:
        return'F'
def main():
    INfilename='C:/Users/wrl123u/Downloads/points.txt'
    Gfilename='C:/Users/wrl123u/Downloads/grades.txt'
    Errfilename='C:/Users/wrl123u/Downloads/error.txt'
    try:
        infile=open(INfilename,'r')
    except Exception as e:
        print('Error opening Points')
        return
    try:
        GIN=open(Gfilename,'w')
        ERIN=open(Errfilename,'w')
    except Exception as e:
        print('Error Opening Files')
        infile.close()
        return
    R=0
    G=0
    E=0
    A=0
    B=0
    C=0
    D=0
    F=0  
    d=date.today()
    t=datetime.now()
    t12H=t.strftime("%I:%M %p")
    print('Program Start:',d,t12H)
    rline=infile.readline()
    while rline != "":
        R+=1
        rline=rline.strip()
        if rline=="":
            rline=infile.readline()
            continue
        fields=rline.split(',')
        if len(fields)!=3:
            ERIN.write(rline+'-Incorrect number of fields')
            E+=1
            rline=infile.readline()
            continue
        id=fields[0].strip()
        name=fields[1].strip()
        pointsF=fields[2].strip()
        try:
            pointsV=int(pointsF)
        except ValueError:
            ERIN.write(f"{id},{name},{pointsF}, -Points are not Numeric"+'\n')
            E +=1
            rline=infile.readline()
            continue
        if pointsV <0 or pointsV > 1000:
            ERIN.write(f"{id},{name},{pointsF}, -Points Out of Range"+'\n')
            E+=1
        else:
            LG=grades(pointsV)
            if LG=='A':
                A+=1
            elif LG=='B':
                B+=1
            elif LG=='C':
                C+=1
            elif LG=='D':
                D+=1
            elif LG=='F':
                F+=1
            GIN.write(f"{id},{name},{pointsF},{LG}"+'\n')
            G+=1
        rline=infile.readline()
    infile.close()
    GIN.close()
    ERIN.close()
    end=date.today()
    endT=datetime.now().strftime("%I:%M %p")
    print('Program Ended at:',end, endT)
    print('Number of Records:',R)
    print('Graded Records:', G)
    print('Errors:',E)
    print("A's:",A)
    print("B's:",B)
    print("C's:",C)
    print("D's:",D)
    print("F's:",F)
main()

