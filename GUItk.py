from pyfirmata import Arduino , SERVO , util
from tkinter import *
import time 
port = 'COM7'
# pin = 8 
board=Arduino(port)
board.digital[8].mode=SERVO
board.digital[9].mode=SERVO
board.digital[10].mode=SERVO
board.digital[11].mode=SERVO
board.digital[12].mode=SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    

# def on_drag(e):
#     bmi = w.get() / (h.get() / 100) ** 2
#     tv_bmi.set(f'BMI = {bmi:.2f}')  # f-strings Python 3.6
#     color_zone = ""
#     if bmi > 30:
#         color_zone = "red"
#     elif bmi >= 25:
#         color_zone = "orange"
#     elif bmi >= 23:
#         color_zone = "yellow"
#     elif bmi >= 18.5:
#         color_zone = "green"
#     else:
#         color_zone = "red"
#     lbl_bmi["bg"] = color_zone

def rotate(e):
    print("1 : " , w.get())
    print("2 : " , h.get())
    print("3 : " , h2.get())
    print("4 : " , h3.get())
    print("5 : " , h4.get())
    rotateservo(8,w.get())
    rotateservo(9,h.get())
    rotateservo(10,h2.get())
    rotateservo(11,h3.get())
    rotateservo(12,h4.get())
    

root = Tk()
root.option_add("*Font", "consolas 20")
tv_bmi = StringVar()
Label(root, text="servo 1").grid(row=0, column=0, sticky="sw", padx=10)
Label(root, text="servo 2").grid(row=1, column=0, sticky="sw", padx=10)
Label(root, text="servo 3").grid(row=2, column=0, sticky="sw", padx=10)
Label(root, text="servo 4").grid(row=3, column=0, sticky="sw", padx=10)
Label(root, text="servo 5").grid(row=4, column=0, sticky="sw", padx=10)



w = Scale(root, from_=1, to=180, orient=HORIZONTAL, length=200, width=30)
w.set(90)
w.grid(row=0, column=1)
w.bind('<B1-Motion>',rotate )
w.bind('<Button-1>',rotate)


h = Scale(root, from_=1, to=180, orient=HORIZONTAL, length=200, width=30)
h.set(90)
h.bind('<B1-Motion>',rotate)
h.bind('<Button-1>',rotate)
h.grid(row=1, column=1)

h2 = Scale(root, from_=1, to=180, orient=HORIZONTAL, length=200, width=30)
h2.set(90)
h2.bind('<B1-Motion>',rotate)
h2.bind('<Button-1>',rotate)
h2.grid(row=2, column=1)

h3 = Scale(root, from_=1, to=180, orient=HORIZONTAL, length=200, width=30)
h3.set(90)
h3.bind('<B1-Motion>',rotate)
h3.bind('<Button-1>',rotate)
h3.grid(row=3, column=1)

h4 = Scale(root, from_=1, to=180, orient=HORIZONTAL, length=200, width=30)
h4.set(90)
h4.bind('<B1-Motion>',rotate)
h4.bind('<Button-1>',rotate)
h4.grid(row=4, column=1)



# lbl_bmi = Label(root, textvariable=tv_bmi)
# lbl_bmi.grid(row=6, columnspan=2, sticky="news")
root.mainloop()