from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

class Vaccine:
    def __init__ (self,root):
        self.root=root
        self.root.title("Covid-19")
        self.root.geometry("900x800+0+0")


        lbtitle=Label(self.root,text="WELCOME TO THE PHARMACY",bd=15,relief=RIDGE,bg="white",fg="darkgreen",font=("cavolini",20,"bold"),padx=2,pady=4)
        lbtitle.pack(side=TOP,fill=X)

        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=900,height=600)
        
        lblcomp=Label(DataFrame,text="PATIENT NAME:",font=("arial",20,"bold"),padx=100,pady=20)
        lblcomp.grid(row=1,column=0,sticky=W)
        txtcomp=Entry(DataFrame,width=29,font=("arial",15,"bold"))
        txtcomp.grid(row=1,column=1)

        

        lblrefno=Label(DataFrame,text="SELECT MEDICINE:",font=("arial",20,"bold"),padx=100,pady=18)
        lblrefno.grid(row=2,column=0,sticky=W)
        ref_combo=ttk.Combobox(DataFrame,width=27,font=("arial",15,"bold"),state='readonly')
        ref_combo["values"]=("CROCIN RS.120","VICKS RS.100","BANDAGE RS.100","DETTOL RS.130","COUGH SYRUP RS.250")
        ref_combo.grid(row=2,column=1)
        ref_combo.current(0)

        lblcomp=Label(DataFrame,text="QUANTITY:",font=("arial",20,"bold"),padx=100,pady=20)
        lblcomp.grid(row=3,column=0,sticky=W)
        txtcomp=Entry(DataFrame,width=29,font=("arial",15,"bold"))
        txtcomp.grid(row=3,column=1)


        lblcomp=Label(DataFrame,text="MOBILE NUMBER",font=("arial",20,"bold"),padx=100,pady=20)
        lblcomp.grid(row=4,column=0,sticky=W)
        txtcomp=Entry(DataFrame,width=29,font=("arial",15,"bold"))
        txtcomp.grid(row=4,column=1)
        

        
        
        btnLogin=Button(DataFrame,text="SUBMIT",width=15,font=('arial',20,'bold'),padx=100,pady=10,bg="white",
                                                                                   command=DataFrame)
                       
        btnLogin.place(x=170,y=400)
       
if __name__ =="__main__":
    root=Tk()
    obj=Vaccine(root)
    root.mainloop()

    
    
