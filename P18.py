from tkinter import*
def CONcel(intext):
    intext=float()
    cel=intext-273.15
    fin=print(cel)
    return fin
def CALbttn(mainwin):
    intext=Entry(mainwin,width=10,bg='white',fg='black',font=('Courier New',32))
    intext.place(x=160,y=500)
    CALbtn=Button(mainwin,font=('Courier New',20),text='CAL',fg='black',bg='gold',command=CONcel(intext))
    CALbtn.place(x=160,y=600)
    return intext
def CEL(fin):
    Cel=Label(font=('Couier New',16),text='Celcius:',fg='black',bg='yellow')
    Cel.place(x=100,y=325)
    Celbox=Entry(width=10,bg='white',fg='black',font=('Courier New',15))
    Celbox.insert(0,fin)
    Celbox.place(x=275,y=325)
def txt(mainwin):
    Kelvin=Label(mainwin,font=('Courier New',16),text='Kalvin:',fg='black',bg='yellow')
    Kelvin.place(x=100,y=250)
    Fah=Label(mainwin,font=('Courier New',16),text='Fahrenheit:',fg='black',bg='yellow')
    Fah.place(x=100,y=400)
def main():
    mainwin=Tk()
    mainwin.geometry('600x800+600+150')
    mainwin.title('Kalvin Converter')
    mainwin.configure(bg='yellow')
    txt(mainwin)
    CEL(mainwin)
    CALbttn(mainwin)
    mainwin.mainloop()
main()


