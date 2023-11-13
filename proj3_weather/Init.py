import fetch_weather as fw
from tkinter import *
import os
from PIL import Image, ImageTk
import requests
from io import BytesIO

def disp_weather():
    location=e1.get()
    unit=v.get()
    url=fw.get_icon()
    url="https:"+url
    new_window = Toplevel(root)
    new_window.geometry("300x200")
    new_window.title("New Window")
    
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    wImg = ImageTk.PhotoImage(img)
    imag = Label(new_window, image=wImg).grid(row=0,column=0)
    #imag.photo = wImg
    #imag.pack()
    #final.config(text="hello")
    # result_text.config(state=NORMAL)
    # result_text.delete(1.0, END)  
    # result_text.insert(END, 'helo')
    # result_text.config(state=DISABLED)
#print(fw.get_temperature("c"))

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "weather/weather.ico")
icon_path=icon_path.replace("\\", "/")

root = Tk()
root.title("Weather")
root.iconbitmap(default=icon_path)
root.geometry("400x300")

Label(root, text='Enter the Location:').grid(row=0, column=0, pady=4, sticky=W)

e1 = Entry(root)
e1.grid(row=0, column=1, pady=5, sticky=W)

v = IntVar()
Label(root,text='Choose a unit:').grid(row=1,column=0,pady=5,sticky=W)
Radiobutton(root, text='Celsius', variable=v, value=1).grid(row=1, column=1, pady=4, sticky=W)
Radiobutton(root, text='Fahrenheit', variable=v, value=2).grid(row=1, column=2, pady=4, sticky=W)

fetch_button = Button(root, text="Find", command=disp_weather)
fetch_button.grid(row=3, column=0, pady=10, columnspan=3)

#result_text = Text(root, height=2, width=20,state= DISABLED)
# final=Label(root,text='')
# final.grid(row=4, column=0, pady=5, sticky=W)
mainloop()
