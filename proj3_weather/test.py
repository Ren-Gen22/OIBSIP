import tkinter as tk
import os

root = tk.Tk()

# Get the absolute path to the ICO file
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "weather.ico")
icon_path=icon_path.replace("\\", "/")
# Set the window icon
print(icon_path)
root.iconbitmap(default=icon_path)

# Continue with your Tkinter application...

root.mainloop()
