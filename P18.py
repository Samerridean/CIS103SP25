from tkinter import *
def kalvin(mainwin,CAL):
    Kelvin=Label(mainwin,font=('Courier New',16),text='Kalvin:',fg='black',bg='yellow')
    Kelvin.place(x=100,y=250)
    Ktxtbox=Entry(mainwin,width=10,bg='white',fg='black',font=('Courier New',15))
    Ktxtbox.place(x=275,y=250)
def CEL(mainwin):
    Cel=Label(font=('Couier New',16),text='Celcius:',fg='black',bg='yellow')
    Cel.place(x=100,y=325)
    Celbox=Entry(width=10,bg='white',fg='black',font=('Courier New',15))
    Celbox.place(x=275,y=325)
def FAH(mainwin):
    Fah=Label(mainwin,font=('Courier New',16),text='Fahrenheit:',fg='black',bg='yellow')
    Fah.place(x=100,y=400)
    Fahbox=Entry(width=10,bg='white',fg='black',font=('Courier New',15))
    Fahbox.place(x=275,y=400)
def CALbttn(mainwin):
    CALbtn=Button(mainwin,font=('Courier New',20),text='CAL',fg='black',
                  bg='gold',command=lambda:CAL(mainwin,kalvin))
    CALbtn.place(x=160,y=600)
def CAL(mainwin,kalvin):
    KtF=kalvin-273.15
    return
def errbox(mainwin):
    error=Entry(mainwin,width=10,bg='white',fg='black',font=('Courier New',32))
    error.place(x=160,y=500)
    clear=Button(mainwin,font=('Courier New',20),text='Clear',fg='Black',bg='gold')
    clear.place(x=300,y=600)
def main():
    mainwin=Tk()
    mainwin.geometry('600x800+600+150')
    mainwin.title('Kalvin Converter')
    mainwin.configure(bg='yellow')
    errbox(mainwin)
    kalvin(mainwin,CAL)
    CEL(mainwin)
    FAH(mainwin)
    CALbttn(mainwin)
    mainwin.mainloop()
main()

