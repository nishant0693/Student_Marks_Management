#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Made By Nishant Singh
# Email:nishant.0693@gmail.com
# Also Contributed: Aarush Mane

import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Marks']
info=mydb.student_info
import json
from tkinter import *
windows=Tk()
from tkinter import messagebox
import tkinter.messagebox
from tkinter import font
global d
global new
new={}
global n
n={}
p={}

 
def close():
    if messagebox.askokcancel("Quit","Do you want to quit"):
        windows.destroy()
def get1():
    global roll_no
    global name
    global english
    global maths
    global physics
    global chemistry
    global biology
    roll_no=e1.get()
    name=e2.get()
    english=e3.get()
    maths=e4.get()
    physics=e5.get()
    chemistry=e6.get()
    biology=e7.get()
 
    if roll_no.isnumeric():
        if name.isalpha():
            if english.isnumeric():
                if maths.isnumeric():
                    if physics.isnumeric():
                        if chemistry.isnumeric():
                            if biology.isnumeric():
                                Item={
                                        "roll_no":roll_no,
                                        "Name":name,
                                        "English":english,
                                        "Maths":maths,
                                        "Physics":physics,
                                        "Chemistry":chemistry,
                                        "Biology":biology
            
                                    }
                                info.insert_one(Item)
                                e1.delete(0,END)
                                e2.delete(0,END)
                                e3.delete(0,END)
                                e4.delete(0,END)
                                e5.delete(0,END)
                                e6.delete(0,END)
                                e7.delete(0,END)
                                
                                                                      
                            else:
                                if len(biology)==0:
                                    messagebox.showinfo("Info","Bilology field should not be empty")
                                else:
                                    messagebox.showinfo("Info","Biology Marks should be a number not alphabet")      
                        else:
                            if len(chemistry)==0:
                                messagebox.showinfo("Info","Chemistry field no should not be empty")
                            else:
                                messagebox.showinfo("Info","Chemistry Marks should be a number not alphabet")    
                    else:
                        if len(physics)==0:
                            messagebox.showinfo("Info","Physics field should not be empty")
                        else:
                            messagebox.showinfo("Info","Physics Marks should be a number not alphabet")
                else:
                    if len(maths)==0:
                        messagebox.showinfo("Info","Maths filed no should not be empty")
                    else:
                        messagebox.showinfo("Info","Maths Marks should be a number not alphabet")
            else:
                if len(english)==0:
                    messagebox.showinfo("Info","English filed should not be empty")
                else:
                    messagebox.showinfo("Info","English Marks should be a number not alphabet")
        else:
            if len(name)==0:
                messagebox.showinfo("Info","Name field no should not be empty")
            else:
                messagebox.showinfo("Info","Name  should be a alphabetr not number")         
    else:
        if len(roll_no)==0:
            messagebox.showinfo("Info","Roll no field should not be empty")
        else:
            messagebox.showinfo("Info","Roll no should be a number not alphabet")
  
myfont=font.Font(family="Helvetics",size=15,weight="bold")
windows.geometry("400x300")
windows.title("Student Marks Entry")
l1=Label(windows,text="Roll No",font=myfont)
l1.grid(row=0,column=0,padx=15)
l2=Label(windows,text="Name",font=myfont)
l2.grid(row=1,column=0,padx=15)
l3=Label(windows,text="English",font=myfont)
l3.grid(row=2,column=0,padx=15)
l4=Label(windows,text="Maths",font=myfont)
l4.grid(row=3,column=0,padx=15)
l5=Label(windows,text="Physics",font=myfont)
l5.grid(row=4,column=0,padx=15)
l6=Label(windows,text="Chemistry",font=myfont)
l6.grid(row=5,column=0,padx=15)
l7=Label(windows,text="Biology",font=myfont)
l7.grid(row=6,column=0,padx=50)
e1=Entry(windows,font=myfont,width=15)
e1.grid(row=0,column=1)
e2=Entry(windows,font=myfont,width=15)
e2.grid(row=1,column=1)
e3=Entry(windows,font=myfont,width=15)
e3.grid(row=2,column=1)
e4=Entry(windows,font=myfont,width=15)
e4.grid(row=3,column=1)
e5=Entry(windows,font=myfont,width=15)
e5.grid(row=4,column=1)
e6=Entry(windows,font=myfont,width=15)
e6.grid(row=5,column=1)
e7=Entry(windows,font=myfont,width=15)
e7.grid(row=6,column=1)
b1=Button(windows,text="Update",activebackground="bisque2",font=myfont,bd=4,command=get1)
b1.grid(row=7,column=0,pady=15)

windows.protocol("WM_DELETE_WINDOW",close)
windows.mainloop()


# In[ ]:




