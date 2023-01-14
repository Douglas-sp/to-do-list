
#import necessary libraries
import tkinter as tk
from tkinter import ttk
import sqlite3

#create the main window
root = tk.Tk()
root.title('To-Do App')

#create database and table
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT, status TEXT)")

#create a frame
frame = tk.Frame(root)
frame.pack()

#create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

#create a listbox
listbox = tk.Listbox(frame, height = 10, width = 40, yscrollcommand = scrollbar.set)
listbox.pack(side = tk.LEFT, fill = tk.BOTH)
scrollbar.config(command = listbox.yview)

#create a label
label1 = tk.Label(root, text = 'Task')
label1.pack()

#create an entry box
entry1 = tk.Entry(root, width = 30)
entry1.pack()

#create a button
button1 = tk.Button(root, text = 'Add Task')
button1.pack()

#create a function to add task to the database
def add_task():
    task = entry1.get()
    c.execute("INSERT INTO todo (task, status) VALUES (?, 'pending')", (task,))
    conn.commit()
    listbox.insert(tk.END, task)

#connect the button to the function
button1.config(command = add_task)

#create a function to delete task from the database
def delete_task():
    task = listbox.get(tk.ACTIVE)
    c.execute("DELETE FROM todo WHERE task = ?", (task,))
    conn.commit()
    listbox.delete(tk.ACTIVE)

#create a delete button
button2 = tk.Button(root, text = 'Delete Task')
button2.pack()

#connect the delete button to the function
button2.config(command = delete_task)

#create a function to update the status of the task
def update_status():
    task = listbox.get(tk.ACTIVE)
    c.execute("UPDATE todo SET status = 'done' WHERE task = ?", (task,))
    conn.commit()

#create a status button
button3 = tk.Button(root, text = 'Update Status')
button3.pack()

#connect the status button to the function
button3.config(command = update_status)

#create a function to populate the listbox
def populate_list():
    c.execute("SELECT task FROM todo")
    tasks = c.fetchall()
    for task in tasks:
        listbox.insert(tk.END, task[0])

#call the populate_list function
populate_list()

#close the database connection
conn.close()

#run the main loop
root.mainloop()