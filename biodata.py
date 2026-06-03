from tkinter import *

root = Tk()
root.title("BIO-DATA FORM")
root.geometry("1000x700")

# Title
title = Label(root, text="BIO-DATA", font=("Arial", 20, "bold"))
title.place(x=500, y=20)

Label(root, text="PERSONAL DATA", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w")

Label(root, text="Name:").place(x=50, y=30)
name = Entry(root, width=30)
name.place(x=100, y=30)

root.mainloop()