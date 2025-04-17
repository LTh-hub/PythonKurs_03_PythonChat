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









#fetch_messages()
root.mainloop()





# git status (frivilligt)
# git add .
# git commit  -m"Added new code for mongo"
# git push


