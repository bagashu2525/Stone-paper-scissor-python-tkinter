from tkinter import *
import random
import PIL
from PIL import Image,ImageTk
from playsound import playsound

root=Tk()
root["bg"]="black"
root.geometry("1450x800")
root.resizable(0,0)
photo =ImageTk.PhotoImage(Image.open("img.jpg"))
l=Label(root,image=photo)
l.place(x=0,y=0,relwidth=1,relheight=1)
global list1
list1=["Stone","paper","scissor"]



def black():
    l=Label(root,text="@@@@@@@@!!!",bg="#99004C",fg="#99004C",font=("clarendon",34))
    l.place(x=560,y=700)
    l=Label(root,text="Computer chooses stone!!!",bg="#000066",fg="#000066",font=("clarendon",24))
    l.place(x=510,y=100)
def play1():
    playsound('success-fanfare-trumpets-6185.mp3')
def play2():
    playsound('failure-drum-sound-effect-2-7184.mp3')
def play3():
    playsound('videogame-death-sound-43894.mp3')
def stone():
    black()
    choice=random.choice(list1)
    if choice=="stone":
        l1=Label(root,text="Computer chooses stone",fg="white",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="MATCH DRAW!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play2()
        
    elif choice=="paper":
        l1=Label(root,text="Computer chooses paper",fg="red",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU lOOSE!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play3()
        
    else:
        l1=Label(root,text="Computer chooses scissor  ",fg="yellow",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU WON!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play1()

def paper():
    black()
    choice=random.choice(list1)
    if choice=="stone":
        l1=Label(root,text="Computer chooses stone  ",fg="yellow",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU WON!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play1()
        
    elif choice=="paper":
        l1=Label(root,text="Computer chooses paper",fg="white",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="MATCH DRAW!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play2()
        
    else:
        l1=Label(root,text="Computer chooses scissor",fg="red",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU lOOSE!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play3()
        

def scissor():
    black()
    choice=random.choice(list1)
    if choice=="stone":
        l1=Label(root,text="Computer chooses stone",fg="red",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU lOOSE!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play3()
        
    elif choice=="paper":
        l1=Label(root,text="Computer chooses paper",fg="yellow",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="YOU WON!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play1()
        
    else:
        l1=Label(root,text="Computer chooses scissor",fg="white",bg="#000066",font=("clarendon",24))
        l1.place(x=510,y=100)
        l1=Label(root,text="MATCH DRAW!!!",fg="yellow",bg="#99004C",font=("clarendon",34))
        l1.place(x=560,y=700)
        play2()
        

name=Label(root,text='This is a stone-Paper-scissor game',font=("Arial",32),bg="#000066",fg="white").pack()
name=Label(root,text='Choose any of the picture as your choice',font=("Arial",24),bg="#000066",fg="cyan").pack()
f=Frame(root)

img_stone=Image.open("stone.png")
resized=img_stone.resize((350,400),Image.ANTIALIAS)
new_stone=ImageTk.PhotoImage(resized)
b1=Button(image=new_stone,command=stone).pack(side=LEFT,padx=50)

img_paper=Image.open("paper.png")
resized=img_paper.resize((350,400),Image.ANTIALIAS)
new_paper=ImageTk.PhotoImage(resized)
b2=Button(image=new_paper,command=paper).pack(side=LEFT,padx=50)

img_scissor=Image.open("scissor.png")
resized=img_scissor.resize((350,400),Image.ANTIALIAS)
new_scissor=ImageTk.PhotoImage(resized)
b3=Button(image=new_scissor,command=scissor).pack(side=LEFT,padx=50)

f.pack()
btn1=Button(root,text='restart the game',command=black,bg="yellow",fg="red",font=("Arial",18))
btn1.place(x=1200,y=700)
root.mainloop()