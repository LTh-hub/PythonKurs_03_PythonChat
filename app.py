# app.py
#
#   Pythonprogrammering för AI-utveckling
#   Kurstillfälle 3 - 16-april-2025
#
#   Utveckling av en Chat med MongoDB
#
#
import tkinter as tk
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["PythonChat"]
messages_col = db["messages"]

# GUI
root = tk.Tk()
root.title("PythonChat")
root.geometry("300x300")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

message_label = tk.Label(root, text="Message: ", justify="left")
message_label.pack()

def fetch_messages():
    messages = messages_col.find().sort("_id")
    message_label.config(text="Messages:\n" + "\n".join(f"- {m['text']}" for m in messages))
    root.after(2000, fetch_messages)        # Var annan sekund mot MongoDB (2000)


fetch_messages()
root.mainloop()



# git status (frivilligt)                   # Behövs inte men visar senaste ändringarna
# git add .                                 # Lägg till allt fr.o.m root till GitHub
# git commit  -m "Ngn lämpligt förkl TxT"   # TxT som visas på GitHub för associerade file
# git push                                  # Pusha upp alla ändringar till GitHub
