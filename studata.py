
"""
Created on Sat Jul  6 22:42:44 2019

@author: INDERDEEP SINGH,HARGOVIND SINGH,IKBIR SINGH
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import *
import sqlite3

conn=sqlite3.connect("project.db")
c = conn.cursor()
window=tk.Tk()

window.geometry("1362x768")
window.config(background='#4040a1')
window.title("BBSBEC STUDENT DATABASE MANAGEMENT SYSTEM")
mainlabel=tk.Label(window, 
		 text="BBSBEC STUDENT DATABASE MANAGEMENT SYSTEM",
		 fg = "white",
         bg=  "#4040a1",
		 font = "verdana 30 bold" ).pack(fill='both',padx=50,pady=10)
#-----------------------------------------------------------------------------------------#
#function for last button
def fbtn6():
    window.destroy()
    
#function for first button
def fbtn1():
    addwindow = tk.Tk()
    addwindow.title("Add New Record")
    addwindow.geometry('1200x700')
    addwindow.config(background='#4040a1')
    tk.Label(addwindow, 
		 text="ADD NEW RECORD",
		 fg = "black",
         bg=  "white",
		 font = "Arial 26 bold ").pack(fill='both',padx=50,pady=10)
    
    l1 = tk.Label(addwindow, text = "Name",bg='#4040a1',fg='white').place(x = 490,y = 190)
    l2 = tk.Label(addwindow, text = "Father Name",bg='#4040a1',fg='white').place(x = 490, y = 230)
    l3 = tk.Label(addwindow, text = "Age",bg='#4040a1',fg='white').place(x = 490, y = 270)
    l4 = tk.Label(addwindow, text = "Roll No",bg='#4040a1',fg='white').place(x = 490, y = 310)
    l5 = tk.Label(addwindow, text = "Department",bg='#4040a1',fg='white').place(x = 490, y = 345)
    l6 = tk.Label(addwindow, text = "Mobile No",bg='#4040a1',fg='white').place(x = 490, y = 390)
    
    comp = tk.StringVar(addwindow)#For 1st dd
    comp.set('Please Pick')
    
    name=tk.StringVar(addwindow)
    fname=tk.StringVar(addwindow)
    age=tk.IntVar(addwindow)
    age.set('')
    rn=tk.IntVar(addwindow)
    rn.set('')
    mbn=tk.IntVar(addwindow)
    mbn.set('')
    
    compound = {'CSE','ELECTRICAL','CIVIL','MECHANICAL','ELECTRONICS'}
    compd = OptionMenu(addwindow, comp, *compound)#For 1st drop down list 
    compd.place(x=580,y=344)
    e1 = tk.Entry(addwindow,textvariable=name).place(x =580 , y = 190)
    e2 = tk.Entry(addwindow,textvariable=fname).place(x = 580, y = 230)
    e3 = tk.Entry(addwindow,textvariable=age).place(x = 580, y = 270)
    e4 = tk.Entry(addwindow,textvariable=rn).place(x = 580, y = 310)
    e6 = tk.Entry(addwindow,textvariable=mbn).place(x = 580, y = 390)
    
    def submit():
        c.execute('INSERT INTO  STUDENT (NAME,FATHER_NAME,AGE,ROLL_NO,DEPARTMENT,MOBILE_NO) VALUES (?, ?, ?,?,?,?)',
                  (name.get(), fname.get(), age.get(),rn.get(),comp.get(),mbn.get()))#Insert record into database.
        conn.commit()
        l12 = tk.Label(addwindow, text = "Record Submitted Successfully",font="arial 20",bg='#4040a1',fg='white').place(x = 430,y = 540)
        comp.set('Please Pick')
        name.set('')
        fname.set('')
        age.set('')
        rn.set('')
        mbn.set('')
        
        
        tk.messagebox.showinfo('INFO','RECORD SUBMITTED SUCCESSFULY')
        

        
    def clear():
        comp.set('Please Pick')
        name.set('')
        fname.set('')
        age.set('')
        rn.set('')
        mbn.set('')
        
    def exit1():
        addwindow.destroy()
    subb = tk.Button(addwindow, text="SUBMIT",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=submit)
    subb.place(x=590,y=440)
    clrbtn=tk.Button(addwindow,text="CLEAR",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=clear)
    clrbtn.place(x=500,y=440)
    exitbtn=tk.Button(addwindow,text="EXIT",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=exit1)
    exitbtn.place(x=550,y=479)
 
#function for 2nd button
def fbtn2():
    updwindow = tk.Tk()
    updwindow.title("Update Record")
    updwindow.geometry('1200x700')
    updwindow.config(background='#4040a1')
    tk.Label(updwindow, 
		 text="UPDATE RECORD",
		 fg = "black",
         bg=  "white",
		 font = "Arial 26 bold ").pack(fill='both',padx=50,pady=10)
    
    l1 = tk.Label(updwindow, text = "Student Roll No",bg='#4040a1',fg='white').place(x = 200,y = 190)
    l2 = tk.Label(updwindow, text = "Select Record",bg='#4040a1',fg='white').place(x = 200, y = 237)
    l3 = tk.Label(updwindow, text = "New Value",bg='#4040a1',fg='white').place(x = 200, y = 280)
                  
    rn=tk.IntVar(updwindow)
    rn.set("")
    newval=StringVar(updwindow)
    
    e1 = tk.Entry(updwindow,textvariable=rn).place(x =300 , y = 190)
    e2 = tk.Entry(updwindow,textvariable=newval).place(x =300 , y = 280)
    comp = tk.StringVar(updwindow)#For 1st dd
    comp.set('Please Pick')
    compound = {'NAME', 'FATHER_NAME', 'AGE','ROLL_NO','DEPARTMENT','MOBILE_NO'}
    compd = OptionMenu(updwindow, comp, *compound)#For 1st drop down list 
    compd.place(x=300,y=230)
    def submitupd():
        c.execute("UPDATE STUDENT SET"+"'"+comp.get()+"'"" = "+"'"+newval.get()+"'"" WHERE ROLL_NO = %d"%rn.get())
        conn.commit()
        c.execute('SELECT * FROM STUDENT WHERE ROLL_NO=%d'%rn.get()) 

        frame = Frame(updwindow)
        frame.place(x= 500, y = 180)
    
        Lb = Listbox(frame, height = 8, width = 70,font=("arial", 10)) 
        Lb.pack(side = LEFT, fill = Y)
    
        scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
        scroll.config(command = Lb.yview)
        scroll.pack(side = RIGHT, fill = Y)
        Lb.config(yscrollcommand = scroll.set) 
    

        Lb.insert(0, 'NAME,FATHER NAME,AGE,ROLL NO,DEPARTMENT,MOBILE NO') #first row in listbox
    
        data = c.fetchall() # Gets the data from the table
    
        for row in data:
            Lb.insert(1,"\n",row) # Inserts record row by row in list box

            L8 = Label(updwindow, text = "UPDATED DATABASE", 
               font=("arial", 16)).place(x=620,y=120)
        conn.commit()
    def clearupd():
        comp.set('Please Pick')
        rn.set('')
        newval.set('')
        
            
    subb = tk.Button(updwindow, text="SUBMIT",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=submitupd)
    subb.place(x=220,y=350)
    exitbtn=tk.Button(updwindow,text="CLEAR",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=clearupd)
    exitbtn.place(x=320,y=350)

#function for 3rd button    
def fbtn3():
    srcwindow = tk.Tk()
    srcwindow.title("Search Record")
    srcwindow.geometry('1200x700')
    srcwindow.config(background='#4040a1')
    tk.Label(srcwindow, 
		 text="SEARCH RECORD",
		 fg = "black",
         bg=  "white",
		 font = "Arial 26 bold ").pack(fill='both',padx=50,pady=10)
    
    l2 = tk.Label(srcwindow, text = "Enter Roll no",bg='#4040a1',fg='white').place(x = 200, y = 239)
                  
    
    val=tk.IntVar(srcwindow)
    val.set("")
    e1 = tk.Entry(srcwindow,textvariable=val).place(x =280 , y=239)

    def submitsrc():
        search="SELECT * FROM STUDENT WHERE ROLL_NO=%d"%val.get()
        c.execute(search)
        conn.commit()
        frame = Frame(srcwindow)
        frame.place(x= 500, y = 180)
    
        Lb = Listbox(frame, height = 8, width = 70,font=("arial", 10)) 
        Lb.pack(side = LEFT, fill = Y)
    
        scroll =Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
        scroll.config(command = Lb.yview)
        scroll.pack(side = RIGHT, fill = Y)
        Lb.config(yscrollcommand = scroll.set) 
    

        Lb.insert(0, 'NAME,FATHER NAME,AGE,ROLL NO,DEPARTMENT,MOBILE NO') #first row in listbox
       
        data = c.fetchall() # Gets the data from the table
        
    
        for row in data:
            Lb.insert(1,"\n",row) # Inserts record row by row in list 

        L8 = Label(srcwindow, text = "RESULT", font=("arial", 16)).place(x=650,y=120)
        conn.commit()
    def clearsrc():
        val.set('')
    
    subb = tk.Button(srcwindow, text="SEARCH",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=submitsrc)
    subb.place(x=210,y=310)
    exitbtn=tk.Button(srcwindow,text="CLEAR",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=clearsrc)
    exitbtn.place(x=310,y=310)
    
def fbtn4():
    delwindow = tk.Tk()
    delwindow.title("Delete Record")
    delwindow.geometry('1200x700')
    delwindow.config(background='#4040a1')
    tk.Label(delwindow, 
		 text="DELETE RECORD",
		 fg = "black",
         bg=  "white",
		 font = "Arial 26 bold ").pack(fill='both',padx=50,pady=10)

    l1 = tk.Label(delwindow, text = "Enter Roll No",bg='#4040a1',fg='white').place(x = 200,y = 240)
                   
    val=tk.IntVar(delwindow)
    val.set("")
    
    e2 = tk.Entry(delwindow,textvariable=val).place(x =300 , y=240)
    
    def subdel():
        delete="DELETE FROM STUDENT WHERE ROLL_NO=(%d)"%val.get()
        c.execute(delete)
        conn.commit()
        frame = Frame(delwindow)
        frame.place(x= 500, y = 180)
    
        L8 = Label(delwindow, text = "RECORD DELETED", 
               font=("arial 30"),fg="white",bg="#4040a1").place(x=660,y=185)
        conn.commit()
    
    def cleardel():
        val.set('')
        
    subb = tk.Button(delwindow, text="DELETE",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=subdel)
    subb.place(x=210,y=310)
    exitbtn=tk.Button(delwindow,text="CLEAR",font='Verdana',bg="#4040a1",fg='white',padx=15,pady=3,command=cleardel)
    exitbtn.place(x=310,y=310)
    
def fbtn5():
    allwindow = tk.Tk()
    allwindow.title("See All Record's")
    allwindow.geometry('1200x700')
    allwindow.config(background='#4040a1')
    tk.Label(allwindow, 
		 text="SEE ALL RECORD'S",
		 fg = "black",
         bg=  "white",
		 font = "Arial 26 bold ").pack(fill='both',padx=50,pady=10)

    c.execute("SELECT * FROM STUDENT") #Select from Student Table
    conn.commit()
    frame = Frame(allwindow)
    frame.place(x= 275, y = 180)
    
    Lb = Listbox(frame, height = 21, width = 65,font=("verdana 13")) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'NAME,FATHER NAME,AGE,ROLL NO,DEPARTMENT,MOBILE NO') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,"-"*83)
        Lb.insert(2,row) # Inserts record row by row in list box
        
    L8 = Label(allwindow, text = "ALL RECORDS",bg='#4040a1',fg='white',
    font=("Verdana 20 bold")).place(x=500,y=120)

    
btn1 = tk.Button(window, text="ADD NEW RECORD",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=62,pady=10,command=fbtn1)
btn1.place(x=500,y=205)

btn2 = tk.Button(window, text="UPDATE RECORD",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=70,pady=10,command=fbtn2)
btn2.place(x=500,y=275)

btn3 = tk.Button(window, text="SEARCH RECORD",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=70,pady=10,command=fbtn3)
btn3.place(x=500,y=345)

btn4 = tk.Button(window, text="DELETE RECORD",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=72,pady=10,command=fbtn4)
btn4.place(x=500,y=415)

btn5 = tk.Button(window, text="SEE ALL RECORD'S",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=63,pady=10,command=fbtn5)
btn5.place(x=500,y=485)

btn6 = tk.Button(window, text="EXIT",font='Verdana',bg="white",fg="#4040a1",activebackground='#4040a1',activeforeground='white',padx=122,pady=10, command=fbtn6)
btn6.place(x=500,y=555)
window.mainloop()