# Execution --
# pip install pyinstaller
# pyinstaller --onefile --windowed app.py

"""
GUI Calculator
"""
from tkinter import *

exp = ""

def press(num):
    global exp
    exp = exp + str(num)
    eq.set(exp)

def clear():
    global exp
    exp = ''
    eq.set("")

def equals():
    global exp
    total = str(eval(exp))
    eq.set(total)
    exp = ''

root = Tk(screenName="Abdul wahab's Calculator")
# root.configure(background="black")
root.geometry("210x250")
root.minsize(210,250)
root.maxsize(210,250)
root.title("AW Calculator")

Label(root,text="Abdul wahab's Calculator",font="Arial 10 bold").pack()
eq = StringVar()
entry = Entry(root,textvariable=eq,bg="white",width=20).pack(fill='both')
f1 = Frame(root,bg='grey')
f1.pack(anchor='w')
button1 = Button(f1, text=' 1 ', bg='silver', command=lambda: press(1),width=5,height=2)
button1.pack(side="left",padx=5) 
button2 = Button(f1,text=' 2 ',command=lambda:press(2),width=5,height=2,bg='silver').pack(side="left",padx=5)
button3 = Button(f1,text=' 3 ',command=lambda:press(3),width=5,height=2,bg='silver').pack(side="left",padx=5)
add = Button(f1,text='+',command=lambda:press("+"),width=5,height=2,bg='silver').pack(side="left",padx=5)

f2 = Frame(root,bg='grey')
f2.pack(anchor='w')
button4 = Button(f2, text=' 4 ', bg='silver', command=lambda: press(4),width=5,height=2)
button4.pack(side="left",padx=5) 
button5 = Button(f2,text=' 5 ',command=lambda:press(5),width=5,height=2,bg='silver').pack(side="left",padx=5)
button6 = Button(f2,text=' 6 ',command=lambda:press(6),width=5,height=2,bg='silver').pack(side="left",padx=5)
add = Button(f2,text='-',command=lambda:press("-"),width=5,height=2,bg='silver').pack(side="left",padx=5)

f3 = Frame(root,bg='grey')
f3.pack(anchor='w')
button7 = Button(f3, text=' 7 ', bg='silver', command=lambda: press(7),width=5,height=2)
button7.pack(side="left",padx=5) 
button8 = Button(f3,text=' 8 ',command=lambda:press(8),width=5,height=2,bg='silver').pack(side="left",padx=5)
button9 = Button(f3,text=' 9 ',command=lambda:press(9),width=5,height=2,bg='silver').pack(side="left",padx=5)
add = Button(f3,text='*',command=lambda:press("*"),width=5,height=2,bg='silver').pack(side="left",padx=5)

f4 = Frame(root,bg='grey')
f4.pack(anchor='w')
button0 = Button(f4, text=' 0 ', bg='silver', command=lambda: press(0),width=5,height=2)
button0.pack(side="left",padx=5) 
buttonDot = Button(f4,text=' . ',command=lambda:press("."),width=5,height=2,bg='silver').pack(side="left",padx=5)
clears = Button(f4,text='Clear',command=clear,width=5,height=2,bg='silver').pack(side="left",padx=5)
div = Button(f4,text='/',command=lambda:press("/"),width=5,height=2,bg='silver').pack(side="left",padx=5)
f5 = Frame(root,bg='grey')
f5.pack(anchor='e',fill='both')
buttonEq = Button(f5,text=' = ',command=equals,width=30,height=20,bg='silver',).pack(padx=5,pady=5,fill='both')

root.mainloop()