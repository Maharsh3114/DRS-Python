import tkinter
import cv2
import PIL.Image, PIL.ImageTk 
from functools import partial #argument dalte hai lekin command ko pata nhi chalta
import threading
import time
import imutils

stream = cv2.VideoCapture("clip.mp4")
def play(speed):
    print(f"You Clicked On Play. Speed is {speed}")

    #play the video in reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    canvas.create_text(132,26, fill="White", font="Times 25  bold",text="Decision Pending")

def pending(decision):
    # 1. Display dp 
    frame = cv2.cvtColor(cv2.imread("DP.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame  = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 2. wait for a sec
    time.sleep(1)
    # 3.display sponsor image
    frame = cv2.cvtColor(cv2.imread("DRSSCREEN.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame  = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 4.wait for 1.5sec
    time.sleep(1.5)
    # 5.Display out or not out
    if decision == 'out':
        decisionImg = "Out.jpg"
    else:
        decisionImg = "Notout.jpg"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame  = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    # 6. wait for 1.5 sec
    

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("The player is Out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("The player is Not Out")

SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("DRS as a Python Project")
cv_img = cv2.cvtColor(cv2.imread("DRSSCREEN.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
canvas.pack()


# buttons to control playback
btn = tkinter.Button(window, text="<< Previous (Fast)", width=50, command=partial(play,-15))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Slow)", width=50, command=partial(play,-2))
btn.pack()
btn = tkinter.Button(window, text="Next (Fast) >>", width=50, command=partial(play,15))
btn.pack()
btn = tkinter.Button(window, text="Next (Slow) >>", width=50, command=partial(play,2))
btn.pack()
btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

window.mainloop()

