import customtkinter as ctk
import tkinter as tk
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

a_width, a_height = 600, 700
root = ctk.CTk()
def submitted():
    admn_no = admnEntry.get()
    name = nameEntry.get()
    classs = classOptionMenu.get()
    age = ageEntry.get()
    f_name = fnameEntry.get()
    gender = genderVar.get()
    ph_no = noentry.get()
    email_id = Emailentry.get()
    address = addressentry.get()
    lst = [admn_no, name, classs, age, f_name, gender, ph_no, email_id, address]
    with open("Student data.csv","a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(lst)
    print(lst)

addFrame = ctk.CTkFrame(root)
addFrame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
add_title = ctk.CTkLabel(addFrame, text='Enter Student Details: ', fg_color="gray30", corner_radius=6, font=("Georgia", 15))
add_title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

root.title("Student Management Program")
root.geometry(f"{a_width}x{a_height}")

# Admission No label
admnLabel = ctk.CTkLabel(addFrame,  text="Admn No")
admnLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

# Admission No field
admnEntry = ctk.CTkEntry(addFrame,  placeholder_text="Enter admn no")
admnEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# Name label
nameLabel = ctk.CTkLabel(addFrame,  text="Name")
nameLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
# Name entry field
nameEntry = ctk.CTkEntry(addFrame,  placeholder_text="Enter your Name")
nameEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# class label
classLabel = ctk.CTkLabel(addFrame,  text="Class")
classLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

# Class combo box
classes = ["LKG", "UKG", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
classOptionMenu = ctk.CTkOptionMenu(addFrame,  values=classes)
classOptionMenu.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

# Age label
ageLabel = ctk.CTkLabel(addFrame,  text="Age")
ageLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
# Age entry field
ageEntry = ctk.CTkEntry(addFrame,  placeholder_text="Enter age")
ageEntry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# Fathers Name label1
fnameLabel = ctk.CTkLabel(addFrame,  text="Fathers Name")
fnameLabel.grid(row=5, column=0, padx=20, pady=20, sticky="ew")


# Fathers Name field
fnameEntry = ctk.CTkEntry(addFrame,  placeholder_text="Enter Fathers Name")
fnameEntry.grid(row=5, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# Gender Label
genderLabel = ctk.CTkLabel(addFrame,  text="Gender")
genderLabel.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
# Gender field
genderVar = tk.StringVar(value="Prefer not to say")
malebutton = ctk.CTkRadioButton(addFrame,  text="Male", variable=genderVar, value="Male")
malebutton.grid(row=6, column=1, padx=20, pady=20, sticky="ew")
femalebutton = ctk.CTkRadioButton(addFrame,  text="Female", variable=genderVar, value="Female")
femalebutton.grid(row=6, column=2, padx=20, pady=20, sticky="ew")
nonebutton = ctk.CTkRadioButton(addFrame,  text="Prefer not to say", variable=genderVar, value="None")
nonebutton.grid(row=6, column=3, padx=20, pady=20, sticky="ew")

# Phone Number label
nolabel = ctk.CTkLabel(addFrame,  text="Phone Number")
nolabel.grid(row=7, column=0, padx=20, pady=20)

# Phone Number field
noentry = ctk.CTkEntry(addFrame,  placeholder_text="Enter Phone number")
noentry.grid(row=7, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# Email id label
Emaillabel = ctk.CTkLabel(addFrame,  text="Email Id")
Emaillabel.grid(row=8, column=0, padx=20, pady=20)

# Email id field
Emailentry = ctk.CTkEntry(addFrame,  placeholder_text="Enter Email Id")
Emailentry.grid(row=8, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

# Address label
addresslabel = ctk.CTkLabel(addFrame, text="Address")
addresslabel.grid(row=9, column=0, padx=20, pady=20)

# Address field
addressentry = ctk.CTkEntry(addFrame,  placeholder_text="Enter Address")
addressentry.grid(row=9, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

submit_btn = ctk.CTkButton(addFrame, text="Submit", command=submitted)
submit_btn.grid(row=10, column=2, columnspan=3, padx=3, pady=3)




root.mainloop()