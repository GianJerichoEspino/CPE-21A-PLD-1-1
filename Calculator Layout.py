from tkinter import *
window = Tk()

#widget section
window.geometry("230x220+850+400")
window.title("Calculator")

#result
lbl = Label(window, text="0", fg="black", font=("Arial",16))
lbl.place(x=180, y=3)

#1st row
ac = Button(window,text="AC", font=("Arial", 12), bd=1, height=1, width=4, fg="darkblue")
ac.place(x=14, y=35)
signage = Button(window, text="+/-", font=("Arial", 12), bd=1, height=1, width=4, fg="darkblue")
signage.place(x=67, y=35)
percent = Button(window, text="%", font=("Arial", 12), bd=1, height=1, width=4, fg="darkblue")
percent.place(x=120, y=35)
divide = Button(window, text="/", font=("Arial", 12), bd=1, height=1, width=4, fg="orange")
divide.place(x=175, y=35)

#2nd row
seven = Button(window,text="7", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
seven.place(x=14, y=70)
eight = Button(window, text="8", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
eight.place(x=67, y=70)
nine = Button(window, text="9", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
nine.place(x=120, y=70)
multiply = Button(window, text="*", font=("Arial", 12), bd=1, height=1, width=4, fg="orange")
multiply.place(x=175, y=70)

#3rd row
four = Button(window,text="4", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
four.place(x=14, y=105)
five = Button(window, text="5", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
five.place(x=67, y=105)
six = Button(window, text="6", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
six.place(x=120, y=105)
minus = Button(window, text="-", font=("Arial", 12), bd=1, height=1, width=4, fg="orange")
minus.place(x=175, y=105)

#4th row
one = Button(window,text="1", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
one.place(x=14, y=140)
two = Button(window, text="2", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
two.place(x=67, y=140)
three = Button(window, text="3", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
three.place(x=120, y=140)
plus = Button(window, text="+", font=("Arial", 12), bd=1, height=1, width=4, fg="orange")
plus.place(x=175, y=140)

#5th row
zero = Button(window,text="0", font=("Arial", 12), bd=1, height=1, width=10, fg="grey")
zero.place(x=14, y=175)
decimal = Button(window, text=".", font=("Arial", 12), bd=1, height=1, width=4, fg="grey")
decimal.place(x=120, y=175)
equals = Button(window, text="=", font=("Arial", 12), bd=1, height=1, width=4, fg="orange")
equals.place(x=175, y=175)

window.mainloop()