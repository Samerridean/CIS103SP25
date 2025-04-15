from tkinter import*
def main():
    mainwin=Tk()
    wcan=Canvas(mainwin,bg='white',width=850,height=800)
    wcan.create_line(150,425,399,427,fill='blue',width=15)
    wcan.create_oval(277,148,400,298,fill='gold',outline='grey',width=10)
    wcan.create_oval(101,148,225,298,fill='silver',outline='orange',width=10)
    wcan.create_oval(7,5,548,525,outline='yellow',width=10)
    wcan.create_line(259,550,374,449,fill='black',width=5)
    wcan.create_line(374,449,151,448,fill='black',width=5)
    wcan.create_line(151,448,259,550,fill='black',width=5)
    wcan.pack()
    mainwin.mainloop()
main()
