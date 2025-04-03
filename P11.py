from datetime import*
from time import*
def main():
    filename='C:/Users/wrl123u/Downloads/points.txt'
    infile=open(filename,'r')
    d=date.today()
    t=datetime.now()
    t12H=t.strftime("%I:%M %p")
    print('Program Start:',d,t12H)
    rline=infile.readline()
    print('Number of Records:',len(rline))
main()

def grade():
    outfile=open(filename,'w')
