#Import All Required Packages
#----------------------------------------->
from tkinter import *
from PIL import Image,ImageTk
from developers import developers
from recognizer_gui import recog_gui
from ocr_gui import ocr_gui
from winsound import *
import random
poklist=["pok.wav","pok2.wav"]
#------------------------------------------->
#Canvas Window Creation
#-------------------------------------------->
#play clicking tune
clicked = lambda: PlaySound(random.choice(poklist),SND_FILENAME)
#--------------------------------------------->
root = Tk()
root.geometry("675x500+120+120")
root.minsize(675,500)
root.maxsize(675,500)
rootwalpaper=Image.open("rootwallpaper.jpg")
bgimg=ImageTk.PhotoImage(rootwalpaper)
canvas=Canvas(root,width=675,height=500)
canvas.pack()
canvas.create_image(335,245,image=bgimg)
root.title("HANDWRITTING RECOGNITION SYSTEM")
pkico=["pok.ico","pok2.ico","pok3.ico"]
root.iconbitmap(random.choice(pkico))
#------------------------------------------------->
#Buttons Section
#-------------------------------------------------->
#Button1---->Hand Written Digits Recognition
#Button2---->OCR
#Button3---->Credits
#Button4---->Exit
b1=Button(root,text="HANWRITTEN \n DIGITS \n RECONGNITION",font=("BankGothic Md BT",13,"bold"),fg="aquamarine",pady=5,padx=5,relief=RAISED,bg="black",command=lambda:[clicked(),recog_gui()])
#place the b1 button
b1_placing=canvas.create_window(222,180,window=b1)
b2=Button(root,text=" OCR ",font=("BankGothic Md BT",18,"bold"),fg="aquamarine",padx=26,pady=18,relief=RAISED,bg="black",command=lambda:[clicked(),ocr_gui()])
#place the b2 button
b2_placing=canvas.create_window(450,180,window=b2)
b3=Button(root,text="DEVELOPERS",font=("BankGothic Md BT",12,"bold"),fg="yellow",pady=20,padx=4,relief=RAISED,bg="black",command=lambda:[clicked(),developers()])
#place the b3 button
b3_placing=canvas.create_window(452,310,window=b3)
b4=Button(root,text=" EXIT ",font=("BankGothic Md BT",25,"bold"),fg="red",padx=31,pady=3,relief=SUNKEN,command=lambda:[clicked(),root.quit()],bg="black")
#place the b4 button
b4_placing=canvas.create_window(220,310,window=b4)
#------------------------------------------------->
#main function
if __name__ == '__main__':
    root.mainloop()