from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if result >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif result >=25:
        labelResult.configure(text="อ้วน")
    elif result >=23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif result >=18.6:
        labelResult.configure(text="น้ำหนักปกติ")
    else:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight =  Label(MainWindow, text="น้ำหนัก")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.grid(row=2, column=-0)
calculateButton.bind('<Button-1>', leftClickButton)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()

