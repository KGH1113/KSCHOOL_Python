from tkinter import *
from tkinter import font
import pyperclip
import random
 
window = Tk()
font1 = font.Font(family="DX유니고딕", size=50)
img1 = PhotoImage(file="img1.png")
img2 = PhotoImage(file="img2.png")
img_title = PhotoImage(file="img_title.png")
 
window.title("K학교전!")
window.geometry("1500x900+100+10")
window.resizable(True, True)
 
title = Label(window, image=img_title)
title.pack()
 
label = Label(window, text="0", font=font1, width=10, height=2)
label.pack()
 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
 
def CopyCode():
    global cnt
 
    list_cnt = []
    for c in str(cnt):
        list_cnt.append(random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + str(ord(c)) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet))
    pyperclip.copy(str(list_cnt))
 
cnt = 0
def countUP():
    global cnt#, image
    cnt += 1
    label.config(text=str(cnt))
    if cnt%2 == 0:
        image.configure(image=img1)
    else:
        image.configure(image=img2)
 
def keyPressHandler(event):
    global cnt, image
    cnt += 1
    label.config(text=str(cnt))
    if cnt%2 == 0:
        image.configure(image=img1)
    else:
        image.configure(image=img2)

def MouseClickHandler(event):
    global cnt, image
    cnt += 1
    label.config(text=str(cnt))
    if cnt%2 == 0:
        image.configure(image=img1)
    else:
        image.configure(image=img2)
 
 
window.bind("<KeyPress>", keyPressHandler)
window.bind("<Button-1>", MouseClickHandler)
 
image = Label(window, image=img1)
image.pack()
 
font2 = font.Font(family="DX유니고딕", size=20)
 
button = Button(overrelief="solid", command=CopyCode, repeatdelay=1, repeatinterval=1000000, text="코드 복사", font=font2)
button.pack()
 
window.mainloop()
