import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
import mysql.connector as csql
from customtkinter import CTkFrame

root = ctk.CTk()

# --------------------------------------------------------------------------------------------------------------- #
# Basic personalization
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
s_size = f"{s_width} x {s_height}"
root.geometry(s_size)

# --------------------------------------------------------------------------------------------------------------- #

# Login Function
def login(new_window):

    # Credentials
    username = "Admin"
    password = "pass"

    # User Entry
    input_username = user_entry.get()
    input_password = user_pass.get()

    # For successful login
    if input_username == username and input_password == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
        print(main_window(login_window))

    else:
        tkmb.showerror("Login Failed", "Invalid username and password.")
# --------------------------------------------------------------------------------------------------------------------#

# Login window
def open_login_window():
    global login_window, user_entry, user_pass
    root.withdraw()
    login_window = ctk.CTkToplevel(root)
    login_window.title("Login")
    login_window.geometry(s_size)
    login_window.state('zoomed')

    # Frame and Buttons for Login Window
    login_frame = ctk.CTkFrame(login_window, width=500, height=1000, corner_radius=15)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(login_frame, text="Login to SMS", font=("Arial", 18, "bold")).pack(pady=20)

    user_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter Username")
    user_entry.pack(pady=10, padx=40, ipadx=30, ipady=5)

    user_pass = ctk.CTkEntry(login_frame, placeholder_text="Enter Password", show="*")
    user_pass.pack(pady=10, padx=40, ipadx=30, ipady=5)

    login_button = ctk.CTkButton(login_frame, text="Login", command=lambda: login(login_window))
    login_button.pack(pady=20, ipadx=20)

    exit_button = ctk.CTkButton(login_frame, text="Exit", command=exit_fn)
    exit_button.pack(pady=5, ipadx=20)

# ------------------------------------------------------------------------------------------------------------------- #

# Main Window with add, edit, view buttons
def main_window(login_window):
    # Main window
    root.deiconify()
    root.state('zoomed')
    login_window.destroy()

    # ============ Buttons =============== #
    btn_frame: CTkFrame = ctk.CTkFrame(root, corner_radius=10, width=s_width//8, height=s_height)
    btn_frame.pack(side=ctk.LEFT)

    fn_frame = ctk.CTkFrame(root, corner_radius=10, width=(s_width-s_width//8), height=s_height)
    fn_frame.pack(side=ctk.RIGHT)

    Add_btn = ctk.CTkButton(btn_frame, text="Add Student Details", width=290, height=50, command=lambda: addinfo_window(fn_frame))
    Add_btn.grid(row=2, column=0, padx=10, pady=10)

    Remove_btn = ctk.CTkButton(btn_frame, text="Edit Student Details", width=290, height=50, command=lambda: edit_student_details(fn_frame))
    Remove_btn.grid(row=3, column=0, padx=10, pady=10)

    Display_btn = ctk.CTkButton(btn_frame, text="Display Student Details", width=290, height=50, command=lambda: view_details(fn_frame))
    Display_btn.grid(row=4, column=0, padx=10, pady=10)

    exit_btn = ctk.CTkButton(btn_frame, text="Logout", width=290, height=50, command=lambda: exit_fn())
    exit_btn.grid(row=5, column=0, padx=10, pady=10)

    appearance_mode_menu = ctk.CTkOptionMenu(btn_frame, values=["Light", "Dark", "System"],
        command=lambda mode: change_mode(root, mode))
    appearance_mode_menu.grid(row=8, column=0, padx=10, pady=100, sticky="s")

    btn_head = ctk.CTkLabel(btn_frame, text='Welcome to SMS ', fg_color="gray30", corner_radius=6, font=("Georgia", 15))
    btn_head.grid(row=0, column=0, padx=5, pady=70, ipady = 20, sticky="ew")

# ------------------------------------------------------------------------------------------------------------------ #

def change_mode(root, new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)


# Add student data side frame
def addinfo_window(Frame):
    add_title = ctk.CTkLabel(Frame, text='Enter Student Details: ', fg_color="gray30", corner_radius=6, font=("Georgia", 15))
    add_title.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="ew")

    root.title("Student Management Program")
    root.geometry(s_size)

    # Scrollable Frame and widgets
    addFrame = ctk.CTkScrollableFrame(Frame, width=(s_width-s_width//8) - 200, height=s_height-100, corner_radius=10)
    addFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    admnLabel = ctk.CTkLabel(addFrame, text="Admission No")
    admnLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    admnEntry = ctk.CTkEntry(addFrame, placeholder_text="Enter Admission No")
    admnEntry.grid(row=1, column=1, columnspan=4, padx=20, pady=20, sticky="ew")

    nameLabel = ctk.CTkLabel(addFrame, text="Name")
    nameLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    nameEntry = ctk.CTkEntry(addFrame, placeholder_text="Enter Name")
    nameEntry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    classLabel = ctk.CTkLabel(addFrame, text="Class")
    classLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    classes = ["LKG", "UKG", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    classOptionMenu = ctk.CTkOptionMenu(addFrame, values=classes)
    classOptionMenu.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

    ageLabel = ctk.CTkLabel(addFrame, text="Age")
    ageLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

    ageEntry = ctk.CTkEntry(addFrame, placeholder_text="Enter Age")
    ageEntry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    fnameLabel = ctk.CTkLabel(addFrame, text="Father's Name")
    fnameLabel.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

    fnameEntry = ctk.CTkEntry(addFrame, placeholder_text="Enter Father's Name")
    fnameEntry.grid(row=5, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    genderLabel = ctk.CTkLabel(addFrame, text="Gender")
    genderLabel.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    genderVar = tk.StringVar(value="Prefer not to say")
    malebutton = ctk.CTkRadioButton(addFrame, text="Male", variable=genderVar, value="Male")
    malebutton.grid(row=6, column=1, padx=20, pady=20, sticky="ew")
    femalebutton = ctk.CTkRadioButton(addFrame, text="Female", variable=genderVar, value="Female")
    femalebutton.grid(row=6, column=2, padx=20, pady=20, sticky="ew")
    nonebutton = ctk.CTkRadioButton(addFrame, text="Prefer not to say", variable=genderVar, value="None")
    nonebutton.grid(row=6, column=3, padx=20, pady=20, sticky="ew")

    nolabel = ctk.CTkLabel(addFrame, text="Phone Number")
    nolabel.grid(row=7, column=0, padx=20, pady=20)

    noentry = ctk.CTkEntry(addFrame, placeholder_text="Enter Phone number")
    noentry.grid(row=7, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    Emaillabel = ctk.CTkLabel(addFrame, text="Email Id")
    Emaillabel.grid(row=8, column=0, padx=20, pady=20)

    Emailentry = ctk.CTkEntry(addFrame, placeholder_text="Enter Email Id")
    Emailentry.grid(row=8, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    addresslabel = ctk.CTkLabel(addFrame, text="Address")
    addresslabel.grid(row=9, column=0, padx=20, pady=20)

    addressentry = ctk.CTkEntry(addFrame, placeholder_text="Enter Address")
    addressentry.grid(row=9, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

    def submit_data():
        student_data = (
            int(admnEntry.get()),
            nameEntry.get(),
            classOptionMenu.get(),
            int(ageEntry.get()),
            fnameEntry.get(),
            genderVar.get(),
            int(noentry.get()),
            Emailentry.get(),
            addressentry.get()
        )
        add_data(student_data)

    submit_btn = ctk.CTkButton(addFrame, text="Submit", command=lambda:submit_data())
    submit_btn.grid(row=10, column=2, columnspan=3, padx=3, pady=3)


# ------------------------------------------------------------------------------------------------------------------ #

def data():
    mydb = csql.connect(
        host="localhost",
        user="root",
        passwd="NSad*1807",
        database="sms"
    )
    mycursor = mydb.cursor()
    mycursor.execute()


def add_data(x):
    mydb = csql.connect(
        host="localhost",
        user="root",
        passwd="NSad*1807",
        database="sms"
    )

    mycursor = mydb.cursor()
    add = """ 
    INSERT INTO students (admn_no, name, class, age, father_name, gender, ph_no, email, address)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mycursor.execute(add, x)
    mydb.commit()
    tkmb.showinfo(title="Success", message="Data Added Successfully")
    addinfo_window()
    mydb.close()

datatype = '''
        admn_no INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        class VARCHAR(4) NOT NULL,
        age INT,
        father_name VARCHAR(50),
        gender VARCHAR(10),
        ph_no BIGINT(10),
        email VARCHAR(255),
        address VARCHAR(255)
        '''

def db_connect():
    try:
        mydb = csql.connect(
            host="localhost",
            user = "root",
            password = "NSad*1807",
            database = "sms"
        )
        return mydb
    except:
        tkmb.showerror("Error", "Couldn't connect to database.")
        return None


def db_data_retriever():

    global data, headers
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    mydb.close()
    return data, headers
    view_details()

# ------------------------------------------------------------------------------------------------------------- #

def view_details(Frame):

    fn_frame = ctk.CTkScrollableFrame(Frame, width=(s_width-s_width//8) - 200, height=s_height-100, corner_radius=10)
    fn_frame.grid(row=1, column=0, padx=10, pady=20, sticky="nsew")

    def resize_canvas(event, table_canvas):
        table_canvas.configure(scrollregion=table_canvas.bbox("both"), background="#2B2B2B", width=(s_width-s_width//8) - 250, height=s_height-150)

    def load_data(table_canvas, table_content):
        global data, headers
        try:

            data, header = db_data_retriever()
            display_table(table_canvas, table_content)

        except Exception as e:
            tkmb.showerror("Error", f"Could not load database: {e}")

    def display_table(table_canvas, table_content):
        global data, headers

        for widget in table_content.winfo_children():
            widget.destroy()

        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(table_content, text=header, font=("Arial", 14, "bold"), padx=20, pady=10)
            header_label.grid(row=0, column=col, sticky="nsew")

        for row, row_data in enumerate(data, start=1):
            for col, cell_data in enumerate(row_data):
                entry = ctk.CTkEntry(table_content, width=200, textvariable=ctk.StringVar(value=cell_data),
                                     state="readonly")
                entry.grid(row=row, column=col, sticky="nsew")

        for col in range(len(headers)):
            table_content.grid_columnconfigure(col, weight=5)

        table_canvas.update_idletasks()
        resize_canvas(None, table_canvas)

    table_frame = ctk.CTkFrame(fn_frame, bg_color="Black")
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Create canvas for the table
    table_canvas = ctk.CTkCanvas(table_frame)
    table_canvas.grid(row=0, column=0, sticky="nsew")

    # Horizontal scrollbar
    scrollbar_x = ctk.CTkScrollbar(table_frame, orientation="horizontal", command=table_canvas.xview)
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    table_canvas.configure(xscrollcommand=scrollbar_x.set)

    # Vertical scrollbar
    scrollbar_y = ctk.CTkScrollbar(table_frame, orientation="vertical", command=table_canvas.yview)
    scrollbar_y.grid(row=0, column=1, sticky="ns",)
    table_canvas.configure(yscrollcommand=scrollbar_y.set)

    # Content inside canvas
    table_content = ctk.CTkFrame(table_canvas)
    table_canvas.create_window((0, 0), window=table_content, anchor="nw")
    table_canvas.bind("<Configure>", lambda event: resize_canvas(event, table_canvas))

    load_data(table_canvas, table_content)

# ------------------------------------------------------------------------------------------------------------- #
def edit_student_details(Frame):
    def search_student(search_entry):
        admn_no = search_entry.get()
        if not admn_no.isdigit():
            tkmb.showerror("Error", "Please enter a valid Admission Number.")
            return

        try:
            mydb = db_connect()
            mycursor = mydb.cursor()
            query = "SELECT * FROM students WHERE admn_no = %s"
            mycursor.execute(query, (admn_no,))
            student = mycursor.fetchone()

            if not student:
                tkmb.showinfo("Not Found", "Student Not Found.")
                return

            name_entry.delete(0, ctk.END)
            name_entry.insert(0, student[1])
            class_entry.set(student[2])
            age_entry.delete(0, ctk.END)
            age_entry.insert(0, student[3])
            father_name_entry.delete(0, ctk.END)
            father_name_entry.insert(0, student[4])
            gender_var.set(student[5])
            phone_entry.delete(0, ctk.END)
            phone_entry.insert(0, student[6])
            email_entry.delete(0, ctk.END)
            email_entry.insert(0, student[7])
            address_entry.delete(0, ctk.END)
            address_entry.insert(0, student[8])

        except Exception as e:
            tkmb.showerror("Error", f"An error occurred: {e}")
        finally:
            mydb.close()

    def update_student():
        admn_no = search_entry.get()
        updated_data = (
            name_entry.get(),
            class_entry.get(),
            age_entry.get(),
            father_name_entry.get(),
            gender_var.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get(),
            admn_no,
        )

        try:
            mydb = db_connect()
            mycursor = mydb.cursor()
            query = """
            UPDATE students
            SET name = %s, class = %s, age = %s, father_name = %s, gender = %s, ph_no = %s, email = %s, address = %s
            WHERE admn_no = %s
            """
            mycursor.execute(query, updated_data)
            mydb.commit()
            tkmb.showinfo("Success", "Student details updated successfully.")
        except Exception as e:
            tkmb.showerror("Error", f"An error occurred: {e}")
        finally:
            mydb.close()


    search_frame = ctk.CTkFrame(Frame, corner_radius=5, height=500, width=800)
    search_frame.grid(row=0, column=0, padx=20, pady=20)

    search_label = ctk.CTkLabel(search_frame, text="Enter Admission Number:", font=("Arial", 14))
    search_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    search_entry = ctk.CTkEntry(search_frame, placeholder_text="Admission Number")
    search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    search_btn = ctk.CTkButton(search_frame, text="Search", command=lambda: search_student(search_entry))
    search_btn.grid(row=0, column=2, padx=10, pady=10)

    fields_frame = ctk.CTkFrame(search_frame, corner_radius=5)
    fields_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_entry = ctk.CTkEntry(fields_frame)
    name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Class:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    class_entry = ctk.CTkOptionMenu(fields_frame, values=["LKG", "UKG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
    class_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    age_entry = ctk.CTkEntry(fields_frame)
    age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Father's Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    father_name_entry = ctk.CTkEntry(fields_frame)
    father_name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Gender:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    gender_var = tk.StringVar(value="Prefer not to say")
    ctk.CTkRadioButton(fields_frame, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, padx=10, pady=5)
    ctk.CTkRadioButton(fields_frame, text="Female", variable=gender_var, value="Female").grid(row=4, column=2, padx=10, pady=5)

    ctk.CTkLabel(fields_frame, text="Phone Number:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    phone_entry = ctk.CTkEntry(fields_frame)
    phone_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Email:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    email_entry = ctk.CTkEntry(fields_frame)
    email_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(fields_frame, text="Address:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    address_entry = ctk.CTkEntry(fields_frame)
    address_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

    update_btn = ctk.CTkButton(fields_frame, text="Update", command=update_student)
    update_btn.grid(row=8, column=0, columnspan=2, pady=10, sticky="ew")

# -------------------------------------------------------------------------------------------------------------- #
def exit_fn():
    root.destroy()

# ---------------------------------------------------------------------------------------------------------------#

open_login_window()
root.mainloop()
