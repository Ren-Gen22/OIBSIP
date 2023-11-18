import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.length_var = tk.StringVar(value="12")
        self.password_var = tk.StringVar()
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.create_widgets()

    def create_widgets(self):
        length_label = ttk.Label(self.root, text="Password Length:")
        length_entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)
        length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        charset_frame = ttk.Frame(self.root)
        charset_label = ttk.Label(charset_frame, text="Character Sets:")
        lowercase_check = ttk.Checkbutton(charset_frame, text="Lowercase", variable=self.lowercase_var)
        uppercase_check = ttk.Checkbutton(charset_frame, text="Uppercase", variable=self.uppercase_var)
        digits_check = ttk.Checkbutton(charset_frame, text="Digits", variable=self.digits_var)
        symbols_check = ttk.Checkbutton(charset_frame, text="Symbols", variable=self.symbols_var)

        charset_label.grid(row=0, column=0, pady=5)
        lowercase_check.grid(row=1, column=0, pady=2, sticky="w")
        uppercase_check.grid(row=2, column=0, pady=2, sticky="w")
        digits_check.grid(row=3, column=0, pady=2, sticky="w")
        symbols_check.grid(row=4, column=0, pady=2, sticky="w")
        charset_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        password_label = ttk.Label(self.root, text="Generated Password:")
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly", justify="center")
        password_label.grid(row=3, column=0, columnspan=2, pady=5)
        password_entry.grid(row=4, column=0, columnspan=2, pady=5)

        copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 7:
                messagebox.showerror("Error", "Password length must be greater than seven.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            return

        character_sets = ""
        if self.lowercase_var.get():
            character_sets += string.ascii_lowercase
        if self.uppercase_var.get():
            character_sets += string.ascii_uppercase
        if self.digits_var.get():
            character_sets += string.digits
        if self.symbols_var.get():
            character_sets += string.punctuation

        if not character_sets:
            messagebox.showerror("Error", "Select at least one character set.")
            return

        password = ''.join(random.choice(character_sets) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "Generate a password first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
