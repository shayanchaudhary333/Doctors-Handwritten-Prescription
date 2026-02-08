import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ------------------ Database Functions ------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shayan@123",  # <-- Put your MySQL password here
        database="userdb"
    )

def insert_user(name, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, password))
    conn.commit()
    conn.close()

def fetch_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    conn.close()
    return results

# ------------------ GUI Functions ------------------
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name == "" or email == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            insert_user(name, email, password)
            messagebox.showinfo("Success", "User Registered Successfully!")
            clear_fields()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

def show_users():
    records = fetch_users()
    output_text.delete("1.0", tk.END)  # Clear previous
    for record in records:
        output_text.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}\n")

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("User Registration")
root.geometry("500x500")
root.config(bg="lightblue")

tk.Label(root, text="Register", font=("Arial", 20), bg="lightblue").pack(pady=10)

tk.Label(root, text="Name:", bg="lightblue").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email:", bg="lightblue").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Password:", bg="lightblue").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

tk.Button(root, text="Register", command=register_user, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Show All Users", command=show_users, bg="blue", fg="white").pack(pady=5)

output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

root.mainloop()
