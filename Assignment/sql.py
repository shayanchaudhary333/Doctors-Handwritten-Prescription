import pymysql

# Step 1: Connect to MySQL (without selecting database)
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Shayan@123'
)
cursor = connection.cursor()

# Step 2: Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS information")
print("Database 'information' created or already exists.")

# Step 3: Select the database
connection.select_db('information')

# Step 4: Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255),
    address VARCHAR(255)
)
""")
print("Table 'customers' is ready.")

# Step 5: Insert multiple records
insert_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
customer_data = [
    ("reem", "borivali"),
    ("riya", "khar"),
    ("reena", "grant road")
]
cursor.executemany(insert_query, customer_data)
connection.commit()

print(cursor.rowcount, "records inserted into 'customers'.")

# Step 6: Close connection
cursor.close()
connection.close()
print("MySQL connection closed.")

import tkinter as tk
from tkinter import messagebox
import pymysql

# ---------- Tkinter UI Setup ----------
r = tk.Tk()
r.geometry("500x500")
r.config(bg="black")
r.title("LOGIN PAGE")
r.minsize(500, 500)
r.maxsize(500, 500)

f = tk.Frame(r, width=300, height=300, bg="white", highlightbackground="blue", highlightthickness=2)
f.place(x=100, y=100)

label = tk.Label(f, text="LOGIN", font=("Helvetica", 16, "bold"), fg="aqua", bg="white")
label.place(x=100, y=20)

first_name_var = tk.StringVar()
label1 = tk.Label(f, text="First Name", font=("Arial", 12), fg="black", bg="white")
label1.place(x=50, y=60)
first_name_entry = tk.Entry(f, textvariable=first_name_var)
first_name_entry.place(x=50, y=90)

last_name_var = tk.StringVar()
label2 = tk.Label(f, text="Last Name", font=("Arial", 12), fg="black", bg="white")
label2.place(x=50, y=120)
last_name_entry = tk.Entry(f, textvariable=last_name_var)
last_name_entry.place(x=50, y=150)

password_var = tk.StringVar()
label3 = tk.Label(f, text="Password", font=("Arial", 12), fg="black", bg="white")
label3.place(x=50, y=180)
password_entry = tk.Entry(f, textvariable=password_var, show="*")
password_entry.place(x=50, y=210)

# ---------- Login Button Action ----------
def login():
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    password = password_var.get()

    if first_name and last_name and password:
        # Step 1: Connect to MySQL (no database selected)
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Shayan@123',
            port=3306
        )
        cursor = connection.cursor()

        # Step 2: Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS information")

        # Step 3: Select the database
        connection.select_db('information')

        # Step 4: Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                password VARCHAR(100)
            )
        """)

        # Step 5: Insert data
        insert_query = "INSERT INTO users (first_name, last_name, password) VALUES (%s, %s, %s)"
        data = (first_name, last_name, password)
        cursor.execute(insert_query, data)
        connection.commit()

        # Confirmation message
        messagebox.showinfo("Login Info", "Login Successful and Data Saved")

        # Step 6: Close connection
        cursor.close()
        connection.close()
    else:
        messagebox.showwarning("Login Info", "Please fill all fields")

# ---------- Login Button ----------
login_button = tk.Button(f, text="Login", command=login, font=("Arial", 12), bg="aqua", fg="black")
login_button.place(x=100, y=250)

r.mainloop()



