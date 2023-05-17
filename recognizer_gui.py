#IMPORT PACKAGES
from tkinter import *
from PIL import Image,ImageTk
from recognizefromvideo import recognize_video,browsevideo
from recognizer import recognize_img,browseimg
import random
from winsound import *
poklist=["pok.wav","pok2.wav"]
clicked=lambda : PlaySound(random.choice(poklist),SND_FILENAME)
def recog_gui():
    lol=Toplevel()
    lol.title("HAND WRITTEN DIGIT RECOGNITION")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    lol.iconbitmap(random.choice(pkico))
    lol.minsize(675,500)
    lol.maxsize(675,500)
    rootwalpaper=Image.open("mini_handWrittenDigitRecognitionWallpaper.jpg")
    bgimg=ImageTk.PhotoImage(rootwalpaper)
    canvas=Canvas(lol,width=675,height=500)
    canvas.pack()
    canvas.create_image(335, 245, image=bgimg)

    b1 = Button(lol, text="RECOGNIZE \nIMAGE", font=("BankGothic Md BT", 16, "bold"), fg="lawn green", pady=1,
                 relief=RAISED, bg="grey15", command=lambda:[clicked(),recognize_img()])
    b1_placing = canvas.create_window(520, 180, window=b1)

    b2 = Button(lol, text="RECOGNIZE \nVIDEO", font=("BankGothic Md BT",16, "bold"), fg="lawn green",  pady=1,
                relief=RAISED, bg="grey15",command=lambda:[clicked(),recognize_video()])
    b2_placing = canvas.create_window(520, 300, window=b2)


    lol.mainloop()

