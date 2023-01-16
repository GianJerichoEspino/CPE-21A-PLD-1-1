from tkinter import *
window = Tk()

# add widgets from here

window.geometry("250x200+760+400")
window.title("My First GUI Application")

# label widget
lbl = Label(window, text="Title", fg="red")
lbl.place(x=120, y=20)

lbl2 = Label(window, text="Field 1:")
lbl2.place(x=30, y=40)

lbl3 = Label(window, text="Field 2:")
lbl3.place(x=30, y=60)

# add button widget
btn = Button(window, text="Yes", fg="Blue", font=("Verdana", 15))
btn.place(x=60, y=100)

btn = Button(window, text="No", fg="Red", font=("Verdana", 15))
btn.place(x=150, y=100)


txtfld1 = Entry(window, text="Text Field 1", bd = 3)
txtfld1.place(x=80, y=40)
txtfld2 = Entry(window, text="Text Field 2", bd = 3)
txtfld2.place(x=80, y=60)

# radio button
def sel():
    selection = "You selected option" + str(var.get())
    label.config(text=selection)
var = IntVar()
radio = Radiobutton(window, text="Male", variable=var, value=1, command=sel)
radio.place(x=5, y=150)

radio2 = Radiobutton(window, text="Female", variable=var, value=2, command=sel)
radio2.place(x=5, y=170)

label = Label(window)
label.place(x=100, y=160)

# toggle button
#check = Checkbutton(window, text="Check")
#check.place(x=80, y=170)

window.mainloop()
