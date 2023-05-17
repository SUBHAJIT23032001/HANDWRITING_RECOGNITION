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
#developers functions....

def biswa():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,265)
    pok.minsize(1000,265)
    pok.title("BISWARUP BHATTACHARJEE")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: BISWARUP BHATTACHARJEE\nENROLLMENT NO: 12019009023003\nROLL: 17\nSECTION: I\nREGISTRATION NO:304201900900848",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
def ankita():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,265)
    pok.minsize(1000,265)
    pok.title("ANKITA SIKDER")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: ANKITA SIKDER\nENROLLMENT NO: 12019009023005\nROLL: 08\nSECTION: I\nREGISTRATION NO:304201900900850",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
def arijit():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,205)
    pok.minsize(1000,205)
    pok.title("ARIJIT GOSWAMI")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: ARIJIT GOSWAMI\nENROLLMENT NO: 12019009001175\nROLL: 11\nSECTION: E",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
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
def rahul():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,205)
    pok.minsize(1000,205)
    pok.title("RAHUL DEBNATH")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: RAHUL DEBNATH\nENROLLMENT NO: 12019009023001\nROLL: 38\nSECTION: D",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
def subhadip():
    pok=Tk()
    pok.geometry("1000x265")
    pok.maxsize(1000,205)
    pok.minsize(1000,205)
    pok.title("SUBHADIP MAJI")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: SUBHADIP MAJI\nENROLLMENT NO: 1201900901345\nROLL: 68\nSECTION: I",bg="black",fg="white",font=("Castellar",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
def allL():
    pok = Tk()
    pok.geometry("1000x270")
    pok.maxsize(1000,270)
    pok.minsize(1000,270)
    pok.title("all Developers")
    pkico = ["pok.ico", "pok2.ico", "pok3.ico"]
    pok.iconbitmap(random.choice(pkico))
    f1 = Frame(pok, bg="black")
    f1=Frame(pok,bg="black")
    fl1=Label(f1,text="NAME: BISWARUP BHATTACHARJEE\nNAME: SUBHAJIT PATI\nNAME: RAHUL DEBNATH\nNAME: ARIJIT GOSWAMI\nNAME: SUBHADIP MAJI\nNAME: ANKITA SIKDER",bg="black",fg="white",font=("BankGothic Md BT",32,"bold"))
    f1.pack(fill="x")
    fl1.pack()
#details of developers......
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
    b1 = Button(rt, text="BISWARUP \n BHATTACHARJEE", font=("BankGothic Md BT", 13, "bold"), fg="black",
                pady=7, padx=7, relief=RAISED, bg="white",command=lambda:[clicked(),biswa()])
    b1_placing = canvas.create_window(180, 80, window=b1)
    b2 = Button(rt, text="ANKITA SIKDER", font=("BankGothic Md BT", 13, "bold"), fg="black", padx=20, pady=12,
                relief=RAISED, bg="white",command=lambda:[clicked(),ankita()])
    b2_placing = canvas.create_window(180, 200, window=b2)
    b3 = Button(rt, text="SUBHAJIT PATI", font=("BankGothic Md BT", 13, "bold"), fg="black", pady=18, padx=22,relief=RAISED,
                bg="white",command=lambda:[clicked(),pati()])
    b3_placing = canvas.create_window(180, 310, window=b3)
    b4 = Button(rt, text="RAHUL \n DEBNATH", font=("BankGothic Md BT", 13, "bold"), fg="black", pady=7, relief=RAISED,
                bg="white",command=lambda:[clicked(),rahul()])
    b4_placing = canvas.create_window(450, 80, window=b4)
    b5 = Button(rt, text="ARIJIT \n GOSWAMI", font=("BankGothic Md BT", 13, "bold"), fg="black", pady=4, relief=RAISED,
                bg="white", command=lambda:[clicked(),arijit()])
    b5_placing = canvas.create_window(448, 200, window=b5)
    b6 = Button(rt, text="SUBHADIP \n MAJI", font=("BankGothic Md BT", 13, "bold"), fg="black", pady=10,
                relief=RAISED,
                bg="white",command=lambda:[clicked(),subhadip()])
    b6_placing = canvas.create_window(448, 310, window=b6)
    b7 = Button(rt, text="IN-SHORT", font=("BankGothic Md BT", 25, "bold"), fg="red", padx=2, pady=1, relief=RAISED,
                command=lambda:[clicked(),allL()], bg="white")
    b7_placing = canvas.create_window(570, 430, window=b7)
    rt.mainloop()