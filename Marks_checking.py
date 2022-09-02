#!/usr/bin/env python
# coding: utf-8

# In[9]:



import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Marks']
info=mydb.student_info
from tkinter import  *
windows=Tk()

from tkinter import messagebox
from tkinter import font
from PIL import Image,ImageTk

myfont=font.Font(family="arial",size=15,weight="bold")
windows.geometry("600x600")
windows.title("Registration form")
image=Image.open("nish.png")
image = image.resize((300, 120))
photo=ImageTk.PhotoImage(image)

lab=Label(image=photo)
lab.place(x=150,y=60)


def get():
    try:
    
        a=e1.get()
        response=info.find_one({'roll_no':a})
        
        

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.insert(2,a)
        e2.insert(0,response['Name'])
        e3.insert(0,response['English'])
        e4.insert(0,response['Maths'])
        e5.insert(0,response['Physics'])
        e6.insert(0,response['Chemistry'])
        e7.insert(0,response['Biology'])
        
    except:
        KeyError()
        messagebox.showinfo("Not found","Roll number not found")      
        
def get1() :
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
def hov(e):
    b1["bg"]="blue"
def hov1(e):
    b1["bg"]="brown"
def hov3(e):
    b2["bg"]="blue"
def hov4(e):
    b2["bg"]="brown"
l1=Label(windows,text="Welcome to Tinkercoders Result ",fg="red",
         bg="Yellow",relief="solid",font=("Helvetica",20,"bold"))
l1.place(x=100,y=10)
l2=Label(windows,text="Roll no:",font=myfont)
l2.place(x=140,y=200)
l3=Label(windows,text="Name:",font=myfont)
l3.place(x=140,y=240)
l4=Label(windows,text="English :",font=myfont)
l4.place(x=140,y=280)
l5=Label(windows,text="Maths :",font=myfont)
l5.place(x=140,y=320)
l6=Label(windows,text="Physics :",font=myfont)
l6.place(x=140,y=360)
l7=Label(windows,text="Chemistry :",font=myfont)
l7.place(x=140,y=400)
l7=Label(windows,text="Biology :",font=myfont)
l7.place(x=140,y=440)
b1=Button(windows,text="Submit",command=get,font=myfont,bg="brown",fg="white")
b1.place(x=160,y=520)
b2=Button(windows,text="Clear",command=get1,font=myfont,bg="brown",fg="white",width=7)
b2.place(x=320,y=520)
e1=Entry(windows,font=myfont)
e1.place(x=280,y=200)
e2=Entry(windows,font=myfont)
e2.place(x=280,y=240)
e3=Entry(windows,font=myfont)
e3.place(x=280,y=280)
e4=Entry(windows,font=myfont)
e4.place(x=280,y=320)
e5=Entry(windows,font=myfont)
e5.place(x=280,y=360)
e6=Entry(windows,font=myfont)
e6.place(x=280,y=400)
e7=Entry(windows,font=myfont)
e7.place(x=280,y=440)

b1.bind("<Enter>",hov)
b1.bind("<Leave>",hov1)
b2.bind("<Enter>",hov3)
b2.bind("<Leave>",hov4)
windows.mainloop()


# In[ ]:




