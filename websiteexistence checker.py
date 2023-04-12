import tkinter as tk
from tkinter import *
import urllib.request

root=Tk()
root.geometry('400x600')
root.title("Check for website Existence")
head=Label(root, text="Lets go ahead check it ", font= ('Bahnschrift Condensed',30),bg="#F08080")
head.place(x=40, y=50)
ur=tk.StringVar()
def check():
    web=(ur.get())
    statcode=urllib.request.urlopen(web).getcode()
    site=statcode==200
    if site==True:
        Label(root,text="Website Available",font=("Bahnschrift Condensed",30)).place(x=100, y=180)
    else:
        Label(root, text="Website is Not Available", font=("Bahnschrift Condensed",30)).place(x=100, y=180)
def destroy():
    root.destroy()
def reset():
    ur.set("")
Entry(root, textvariable=ur,width=50).place(x=40,y=150)
Button(root, text='Check',font=('Bahnschrift Condensed',25),command=check).place(x=20,y=290)
Button(root,text='Reset',font=("Bahnschrift Condensed",25),command=reset).place(x=180,y=290)
Button(root,text="Exit",font=("Bahnschrift Condensed",25),command=destroy).place(x=60,y=400)
root.mainloop()
