
from tkinter import *
from tkinter import messagebox

root = Tk()

# code to add widgets and style window will go here
root.geometry("450x400")
root.title("Malaysia trip (Gary)")


# variables
results = IntVar()


Label(root, text="Amount: ").place(x=10, y=70)
user_ent = Entry(root)
user_ent.place(x=120, y=70)
user_ent.focus()
# res_lab = Label(root, text="", textvariable=results)
# res_lab.place(x=150, y=230)


def error():
    try:
        amount = 3000
        if int(user_ent.get()) >= amount:
            messagebox.showinfo('status', 'you qualify')
    except ValueError:
        if user_ent.get() != int:
            messagebox.showerror('error', 'invalid data type')
    else:
        if int(user_ent.get()) < amount:
            messagebox.showerror('error', 'you do not meet the terms')


Button(root, text="submit", borderwidth=3, command=error).place(x=170, y=180)


root.mainloop() 
