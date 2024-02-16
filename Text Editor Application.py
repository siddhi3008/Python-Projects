import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text. delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        with open(file_path, "r") as file:
            text. delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Info","File saves successfully")

root = tk.Tk()
root.title("Text Editor Application")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu= file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text= tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="red")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()

