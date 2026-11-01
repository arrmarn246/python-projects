
from tkinter import *

def press_button(num):
    global equation_text

    equation_text = equation_text+str(num)#the problem was this line not ""+ it will only throw one value 
    equation_label.set(equation_text)

def equal():#no parameter needed
    global equation_text
    try:
        num = eval(equation_text)

        equation_text = str(num)
   
        equation_label.set(num)
    except ZeroDivisionError:
        equation_text = ""
        equation_label.set("Error")

    except SyntaxError:
        equation_text=""
        equation_label.set("Error")
        
def clear():
    global equation_text

    equation_text=""
    equation_label.set(equation_text)



window = Tk()
window.title("Calculator")
window.geometry("500x500")



equation_text = ""
equation_label = StringVar()

label = Label(window,textvariable = equation_label,font=('Consolas',20),width=30,height=2,bg="pink")#window textvariable= ....
label.pack()

frame = Frame(window)#label out mhr htar ya tr
frame.pack()

button1 = Button(frame,text="1",bg="white",width=9,height=2,font =35,command= lambda: press_button(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text="2",bg="white",width=9,height=2,font =35,command= lambda: press_button(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text="3",bg="white",width=9,height=2,font =35,command= lambda: press_button(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text="4",bg="white",width=9,height=2,font =35,command= lambda: press_button(4))
button4.grid(row=0,column=3)

button5 = Button(frame,text="5",bg="white",width=9,height=2,font =35,command= lambda: press_button(5))
button5.grid(row=1,column=0)

button6 = Button(frame,text="6",bg="white",width=9,height=2,font =35,command= lambda: press_button(6))
button6.grid(row=1,column=1)

button7 = Button(frame,text="7",bg="white",width=9,height=2,font =35,command= lambda: press_button(7))
button7.grid(row=1,column=2)

button8 = Button(frame,text="8",bg="white",width=9,height=2,font =35,command= lambda: press_button(8))
button8.grid(row=1,column=3)

button9 = Button(frame,text="9",bg="white",width=9,height=2,font =35,command= lambda: press_button(9))
button9.grid(row=3,column=0)

button0 = Button(frame,text="0",bg="white",width=9,height=2,font =35,command= lambda: press_button(0))
button0.grid(row=3,column=1)

decimal = Button(frame,text=".",bg="white",width=9,height=2,font =35,command= lambda: press_button("."))
decimal.grid(row=3,column=2)

plus = Button(frame,text="+",bg="white",width=9,height=2,font =35,command= lambda: press_button("+"))
plus.grid(row=3,column=3)

minus = Button(frame,text="-",bg="white",width=9,height=2,font =35,command= lambda: press_button("-"))
minus.grid(row=4,column=0)

multiply = Button(frame,text="x",bg="white",width=9,height=2,font =35,command= lambda: press_button("*"))
multiply.grid(row=4,column=1)

division = Button(frame,text="/",bg="white",width=9,height=2,font =35,command= lambda: press_button("/"))
division.grid(row=4,column=2)

equal = Button(frame,bg="white",text="=",width=9,height=2,font =35,command= equal)
equal.grid(row=4,column=3)

clear = Button(frame,bg="white",text="clear",width=9,height=2,font =35,command= clear)
clear.grid(row=6,column=1)

window.mainloop()
