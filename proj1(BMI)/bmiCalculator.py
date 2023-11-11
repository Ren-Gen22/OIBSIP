from tkinter import *

def calculate_bmi():
    try:
        unit = v.get()
        weight = float(e1.get())
        height = float(e2.get())
        if unit ==1:
            height/=100
        if unit == 2:
            height *= 0.3048
        
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            stat = "Underweight"
        elif 18.5 <= bmi < 25.0:
            stat = "Healthy"
        elif 25.0 <= bmi < 30.0:
            stat = "Overweight"
        else:
            stat = "Obese"

        result_text.delete(1.0, END)  
        result_text.insert(END, f'Result\nYour BMI: {bmi:.2f}\nStatus: {stat}')

    except ValueError:
        result_text.delete(1.0, END)  
        result_text.insert(END, "Error: Please enter valid numeric values for weight and height.")

root = Tk()
root.title("BMI Calculator")

root.geometry("300x300")

Label(root, text='Height in:').grid(row=0, column=0, pady=5, sticky=W)
Label(root, text='Weight (kg):').grid(row=1, column=0, pady=5, sticky=W)
Label(root, text='Height:').grid(row=2, column=0, pady=5, sticky=W)

v = IntVar()
Radiobutton(root, text='Centimeter', variable=v, value=1).grid(row=0, column=1, pady=5, sticky=W)
Radiobutton(root, text='Feet', variable=v, value=2).grid(row=0, column=2, pady=5, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=1, column=1, pady=5, sticky=W)
e2.grid(row=2, column=1, pady=5, sticky=W)

calculate_button = Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, pady=10, columnspan=3)

result_text = Text(root, height=5, width=30)
result_text.grid(row=4, column=0, pady=5, columnspan=3, sticky=W)

mainloop()
