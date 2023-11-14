import fetch_weather as fw
from tkinter import *
import os
from PIL import Image, ImageTk
def current_dir(a,b="",c=""):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if b!="":
        icon_path = os.path.join(script_dir, a,b,c)
    else:
        icon_path = os.path.join(script_dir, a)    
    icon_path=icon_path.replace("\\", "/")
    return icon_path

def disp_weather():
    location=e1.get()
    unit=v.get()
    url=fw.get_icon()
    conditon=fw.get_conditon()
    Temp,feelTemp=fw.get_temperature(unit)
    split_url=url.split("/")
    time=split_url[len(split_url)-2] 
    logo=split_url[len(split_url)-1]
    wImg=current_dir("weatherImg",time,logo)
    #print(wImg)

    image_window = Toplevel(root)
    image_window.geometry("300x300")
    img = Image.open(wImg)
    img = ImageTk.PhotoImage(img)
    image = Label(image_window, image=img)
    image.image = img  
    image.pack(side=TOP)

    Label(image_window,text=conditon).pack(side=TOP)
    Label(image_window,text=Temp).pack(side=TOP)
    Label(image_window,text=feelTemp).pack(side=TOP)






icon_path=current_dir("weatherImg/weather.ico")
root = Tk()
root.title("Weather")
root.iconbitmap(default=icon_path)
root.geometry("400x100")

Label(root, text='Enter the Location:').grid(row=0, column=0, pady=4, sticky=W)

e1 = Entry(root)
e1.grid(row=0, column=1, pady=5, sticky=W)

v = IntVar()
Label(root,text='Choose a unit:').grid(row=1,column=0,pady=5,sticky=W)
Radiobutton(root, text='Celsius', variable=v, value=0).grid(row=1, column=1, pady=4, sticky=W)
Radiobutton(root, text='Fahrenheit', variable=v, value=1).grid(row=1, column=2, pady=4, sticky=W)

fetch_button = Button(root, text="Find", command=disp_weather)
fetch_button.grid(row=3, column=0, pady=10, columnspan=3)

mainloop()
