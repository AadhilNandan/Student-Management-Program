import mysql.connector
import customtkinter as ctk
from tkinter import messagebox

# Initialize the root window
root = ctk.CTk()

# Global variables
headers = []
data = []

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'NSad*1807',
    'database': 'sms'
}


def connect_to_db():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", f"Error connecting to database: {e}")
        return None


def load_data_from_db():
    global data, headers
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        headers = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        connection.close()
        display_table()



def save_data_to_db():
    global data, headers
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        for row_index, row_data in enumerate(data):
            update_query = f"UPDATE students SET "  # Modify with your actual table name
            update_query += ", ".join([f"{headers[col_index]} = %s" for col_index in range(len(row_data))])
            update_query += f" WHERE id = %s"  # Assuming 'id' is the primary key, modify if needed
            cursor.execute(update_query, tuple(row_data + [row_data[0]]))  # Including the ID for the WHERE clause
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Data saved successfully!")


# Function to update a specific cell value when it loses focus
def update_cell_value(row, col, new_value):
    global data
    data[row][col] = new_value


# Function to display data in a table format
def display_table():
    global data, headers
    for widget in table_content.winfo_children():
        widget.destroy()

    # Display headers
    for col, header in enumerate(headers):
        header_label = ctk.CTkLabel(table_content, text=header, font=("Arial", 14, "bold"), padx=10, pady=5)
        header_label.grid(row=0, column=col, sticky="nsew")

    # Display data rows
    for row, row_data in enumerate(data, start=1):
        for col, cell_data in enumerate(row_data):
            entry = ctk.CTkEntry(table_content, width=150, textvariable=ctk.StringVar(value=cell_data))
            entry.grid(row=row, column=col, sticky="nsew")
            entry.bind("<FocusOut>", lambda e, r=row, c=col: update_cell_value(r, c, e.widget.get()))

    # Configure column weights to make the table responsive
    for col in range(len(headers)):
        table_content.grid_columnconfigure(col, weight=1)


# Function to create the view window
def open_view_window():
    global table_content

    view_window = ctk.CTkToplevel(root)
    view_window.title("MySQL Excel-like Viewer")

    # Set window to full screen
    screen_width = view_window.winfo_screenwidth()
    screen_height = view_window.winfo_screenheight()
    view_window.geometry(f"{screen_width}x{screen_height}")

    # Create header frame for buttons
    header_frame = ctk.CTkFrame(view_window)
    header_frame.pack(fill="x", pady=5)

    # Load and Save buttons
    load_button = ctk.CTkButton(header_frame, text="Load Data", command=load_data_from_db)
    load_button.pack(side="left", padx=5)

    save_button = ctk.CTkButton(header_frame, text="Save Data", command=save_data_to_db)
    save_button.pack(side="left", padx=5)

    # Create a table frame to hold the table
    table_frame = ctk.CTkFrame(view_window)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # Create a canvas with vertical scrollbar
    table_canvas = ctk.CTkCanvas(table_frame)
    table_canvas.pack(side="left", fill="both", expand=True)
    scrollbar = ctk.CTkScrollbar(table_frame, orientation="vertical", command=table_canvas.yview)
    scrollbar.pack(side="right", fill="y")
    table_canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the table content
    table_content = ctk.CTkFrame(table_canvas)
    table_canvas.create_window((0, 0), window=table_content, anchor="nw")

    # Bind resize event for the canvas
    table_canvas.bind("<Configure>", lambda event: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    # Display the table after loading the data
    display_table()


# Main UI setup
def main():
    root.title("MySQL Table Viewer")
    root.geometry("800x600")

    # Create buttons to open view window
    open_button = ctk.CTkButton(root, text="Open View Window", command=open_view_window)
    open_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
