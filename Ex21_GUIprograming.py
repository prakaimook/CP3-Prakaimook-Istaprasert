from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)

    if bmi >= 30:
        result = "อ้วนมาก"
    elif bmi >=25:
        result="อ้วน"
    elif bmi >=23:
        result="น้ำหนักเกิน"
    elif bmi >=18.6:
        result="น้ำหนักปกติ"
    else:
        result="ผอมเกินไป"
    labelResult.configure(text=bmi)
    labelResult2.configure(text=result)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight =  Label(MainWindow, text="น้ำหนัก (kb)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.grid(row=2, column=-0)
calculateButton.bind('<Button-1>', leftClickButton)
labelResult = Label(MainWindow,text="BMI")
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow,text="ผลลัพธ์")
labelResult2.grid(row=3,column=1)

MainWindow.mainloop()

