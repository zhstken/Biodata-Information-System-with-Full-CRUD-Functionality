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

from tkinter import *

root = Tk()
root.title("BIO-DATA FORM")
root.geometry("1000x700")

# Title
title = Label(root, text="BIO-DATA", font=("Arial", 20, "bold"))
title.grid(row=0, column=0, columnspan=4, pady=10, padx=500)

# ---------- PERSONAL DATA ----------
Label(root, text="PERSONAL DATA", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w")

# Left side
Label(root, text="Name:").grid(row=2, column=0, sticky="w")
name = Entry(root, width=30)
name.grid(row=2, column=1)

Label(root, text="Gender:").grid(row=3, column=0, sticky="w")
gender = Entry(root, width=30)
gender.grid(row=3, column=1)

Label(root, text="Date of Birth:").grid(row=4, column=0, sticky="w")
dob = Entry(root, width=30)
dob.grid(row=4, column=1)

Label(root, text="Current Address:").grid(row=5, column=0, sticky="w")
address = Entry(root, width=30)
address.grid(row=5, column=1)

Label(root, text="Age:").grid(row=6, column=0, sticky="w")
age = Entry(root, width=30)
age.grid(row=6, column=1)

Label(root, text="Civil Status:").grid(row=7, column=0, sticky="w")
status = Entry(root, width=30)
status.grid(row=7, column=1)

Label(root, text="Contact No:").grid(row=8, column=0, sticky="w")
contact = Entry(root, width=30)
contact.grid(row=8, column=1)

Label(root, text="Email:").grid(row=9, column=0, sticky="w")
email = Entry(root, width=30)
email.grid(row=9, column=1)

# Right side fields
Label(root, text="Citizenship:").grid(row=2, column=2, sticky="w")
citizenship = Entry(root, width=25)
citizenship.grid(row=2, column=3)

Label(root, text="Religion:").grid(row=3, column=2, sticky="w")
religion = Entry(root, width=25)
religion.grid(row=3, column=3)

Label(root, text="Occupation:").grid(row=4, column=2, sticky="w")
occupation = Entry(root, width=25)
occupation.grid(row=4, column=3)

Label(root, text="Telephone:").grid(row=5, column=2, sticky="w")
telephone = Entry(root, width=25)
telephone.grid(row=5, column=3)

Label(root, text="Place of Birth:").grid(row=6, column=2, sticky="w")
pob = Entry(root, width=25)
pob.grid(row=6, column=3)

# ---------- EDUCATION ----------
Label(root, text="EDUCATIONAL BACKGROUND", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", pady=10)

Label(root, text="Elementary:").grid(row=11, column=0, sticky="w")
elem = Entry(root, width=40)
elem.grid(row=11, column=1)

Label(root, text="High School:").grid(row=12, column=0, sticky="w")
hs = Entry(root, width=40)
hs.grid(row=12, column=1)

Label(root, text="College:").grid(row=13, column=0, sticky="w")
college = Entry(root, width=40)
college.grid(row=13, column=1)

# Button
def submit():
    print("Data Saved!")

Button(root, text="Submit", command=submit, bg="green", fg="white").grid(row=14, column=1, pady=20)

root.mainloop()
root.mainloop()