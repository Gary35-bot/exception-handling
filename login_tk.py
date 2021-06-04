from tkinter import *
from tkinter import messagebox

root = Tk()


root.geometry("450x400")
root.title("Login Info (Gary)")

# set frame for content
result = StringVar()
tick_btn = StringVar()


Label(root, text="Login Info").place(x=200, y=20)

Label(root, text="Username: ").place(x=10, y=70)
user_ent = Entry(root)
user_ent.place(x=120, y=70)
user_ent.focus()
Label(root, text="Password: ").place(x=10, y=130)
pass_ent = Entry(root, show="\u2022")
pass_ent.place(x=120, y=130)
res_lab = Label(root, text="", textvariable=result)
res_lab.place(x=150, y=230)


def log_in():
    usernames = ["Gary", "Cassiem", "Zaid", "Aaliyah"]
    passwords = ["1111", "5454", "0000", "binary101"]

    found = False

    for x in range(len(usernames)):
        if user_ent.get() == usernames[x] and pass_ent.get() == passwords[x]:
            found = True

    if found:
        result.set("Welcome Madam/Sir!")
        root.destroy()
        import login_page2
    else:
        result.set("Access Denied!!!")


def clear():
    user_ent.delete(0, END)
    pass_ent.delete(0, END)
    result.set("")


def kill():
    root.destroy()


def toggle_password():
    global pass_ent, tick
    if tick_btn.get():
        pass_ent['show'] = ""
    else:
        pass_ent['do not show'] = ""


# create Buttons
Button(root, text="Login", borderwidth=3, command=log_in).place(x=170, y=180)
Button(root, text="Clear", borderwidth=3, command=clear).place(x=170, y=280)
Button(root, text="Exit", borderwidth=3, command=kill).place(x=170, y=330)
tick = Checkbutton(root, onvalue=True, offvalue=False, textvariable=tick_btn, command=toggle_password)
tick.place(x=300, y=130)


root.mainloop()
