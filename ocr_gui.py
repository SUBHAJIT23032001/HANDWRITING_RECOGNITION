#IMPORT PACKAGES
from tkinter import *
from PIL import Image,ImageTk
import random
from winsound import  *
poklist=["pok.wav","pok2.wav"]
clicked=lambda:PlaySound(random.choice(poklist),SND_FILENAME)
from ocrecog import analyze_img
def ocr_gui():
    listii=["ocr.jpg","ocrwallpaper.jpg"]
    lol=Toplevel()
    lol.title("HAND WRITTEN DIGIT RECOGNITION")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    lol.iconbitmap(random.choice(pkico))
    lol.minsize(675,500)
    lol.maxsize(675,500)
    rootwalpaper=Image.open(random.choice(listii))
    bgimg=ImageTk.PhotoImage(rootwalpaper)
    canvas=Canvas(lol,width=675,height=500)
    canvas.pack()
    canvas.create_image(335, 245, image=bgimg)

    b1 = Button(lol, text="RECOGNIZE \nIMAGE", font=("BankGothic Md BT", 18, "bold"), fg="lawn green", pady=2,
                 relief=RAISED, bg="grey15", command=lambda:[clicked(),analyze_img()])
    b1_placing = canvas.create_window(530, 180, window=b1)


    lol.mainloop()
