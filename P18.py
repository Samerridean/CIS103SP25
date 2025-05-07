from tkinter import *
import math

def kelvin(mainwin):
    Kelvin = Label(mainwin, font=('Courier New', 16), text='Kelvin:', fg='black', bg='yellow')
    Kelvin.place(x=100, y=250)   
    Ktxtbox = Entry(mainwin, width=10, bg='white', fg='black', font=('Courier New', 15))
    Ktxtbox.place(x=275, y=250)  
    return Ktxtbox
def celsius(mainwin):
    Cel = Label(mainwin, font=('Courier New', 16), text='Celsius:', fg='black', bg='yellow')
    Cel.place(x=100, y=325)   
    Celbox = Entry(mainwin, width=10, bg='white', fg='black', font=('Courier New', 15))
    Celbox.place(x=275, y=325)    
    return Celbox
def fahrenheit(mainwin):
    Fah = Label(mainwin, font=('Courier New', 16), text='Fahrenheit:', fg='black', bg='yellow')
    Fah.place(x=100, y=400)   
    Fahbox = Entry(mainwin, width=10, bg='white', fg='black', font=('Courier New', 15))
    Fahbox.place(x=275, y=400) 
    return Fahbox
def calculate(Ktxtbox, Celbox, Fahbox, errbox):
    try:
        input_text = Ktxtbox.get()
        if not input_text:
            raise ValueError("Cannot Be Blank")
        num = float(input_text)
        if num <= 0:
           raise ValueError("Kelvin Cannot Be Negative Or Zero")
        Celbox.delete(0, END)
        Fahbox.delete(0, END)
        cel_value = num - 273.15
        fah_value = (cel_value * 9/5) + 32
        Celbox.insert(0, f"{cel_value:.2f}")
        Fahbox.insert(0, f"{fah_value:.2f}")
    except ValueError as e:
        errbox.delete(0, END)
        errbox.insert(0, str(e))
def clear_boxes(Ktxtbox, Celbox, Fahbox, errbox):
    Ktxtbox.delete(0, END)
    Celbox.delete(0, END)
    Fahbox.delete(0, END)
    errbox.delete(0, END)
def buttons(mainwin, Ktxtbox, Celbox, Fahbox, errbox):
    CALbtn = Button(mainwin, font=('Courier New', 20), text='CAL', fg='black',
                    bg='gold', command=lambda: calculate(Ktxtbox, Celbox, Fahbox, errbox))
    CALbtn.place(x=160, y=600)   
    Clearbtn = Button(mainwin, font=('Courier New', 20), text='Clear', fg='black',
                      bg='gold', command=lambda: clear_boxes(Ktxtbox, Celbox, Fahbox, errbox))
    Clearbtn.place(x=300, y=600)
def errbox(mainwin):
    err_entry = Entry(mainwin, width=20, bg='white', fg='black', font=('Courier New', 16))
    err_entry.place(x=160, y=500)
    return err_entry
def main():
    mainwin = Tk()
    mainwin.geometry('600x800+600+150')
    mainwin.title('Kelvin Converter')
    mainwin.configure(bg='yellow')
    Ktxtbox = kelvin(mainwin)
    Celbox = celsius(mainwin)
    Fahbox = fahrenheit(mainwin)
    err_entry = errbox(mainwin)
    buttons(mainwin, Ktxtbox, Celbox, Fahbox, err_entry)
    mainwin.mainloop()
main()
