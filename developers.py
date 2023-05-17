#Import ALL packages
from tkinter import *
from PIL import  Image,ImageTk
import random
from winsound import *
#--------------------------->
#clicking sound
poklist=["pok.wav","pok2.wav"]
clicked=lambda:PlaySound(random.choice(poklist),SND_FILENAME)
#----------------------------->
#developer functions....


def pati():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,205)
    pok.minsize(1000,205)
    pok.title("SUBHAJIT PATI")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: SUBHAJIT PATI\nENROLLMENT NO: 12019009023006\nROLL: 68\nSECTION: C",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()


#details of developer......
def developers():
    listwalp=["mini_developerswalp.jpg","mini_img.jpg","mini_img1.jpg","mini_img2.jpg","mini_img3.jpg","mini_img4.jpg","mini_img5.jpg"]
    rt=Toplevel()
    rt.title("DEVELOPERS")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    rt.iconbitmap(random.choice(pkico))
    rt.geometry("675x500+120+120")
    rt.minsize(675,500)
    rt.maxsize(675,500)
    rootwalpaper=Image.open(random.choice(listwalp))
    bgimg=ImageTk.PhotoImage(rootwalpaper)
    canvas=Canvas(rt,width=675,height=500)
    canvas.pack()
    canvas.create_image(335,245,image=bgimg)
    
    b3 = Button(rt, text="SUBHAJIT PATI", font=("BankGothic Md BT", 13, "bold"), fg="black", pady=18, padx=22,relief=RAISED,
                bg="white",command=lambda:[clicked(),pati()])
    b3_placing = canvas.create_window(180, 310, window=b3)
    
    rt.mainloop()
