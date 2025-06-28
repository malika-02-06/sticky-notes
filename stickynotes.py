import tkinter as tk
from tkinter import messagebox
import os

# 🌷 Create main app window
root = tk.Tk()
root.title("Sticky Note Queen 💖")
root.geometry("300x400")
root.config(bg="#fff0f5")  # pastel pink

# 💌 Text area
text_area = tk.Text(root, wrap='word', font=("Arial", 12), bg="#fffafc", fg="#333")
text_area.pack(expand=True, fill='both', padx=10, pady=10)

# 💾 Save note function
def save_note():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        with open("my_note.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Your magical note has been saved ✨")
    else:
        messagebox.showwarning("Oops!", "Your note is empty!")

# 🩷 Button to save
save_btn = tk.Button(root, text="Save Note💟", command = save_note, bg="#ffc0cb", fg="white", font=("Arial", 11, "bold"))
save_btn.pack(pady=10)

# 🍭 Load existing note if any
if os.path.exists("my_note.txt"):
    with open("my_note.txt", "r", encoding="utf-8") as f:
        text_area.insert("1.0", f.read())

root.mainloop()








