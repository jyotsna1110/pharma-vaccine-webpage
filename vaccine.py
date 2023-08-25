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


        lbtitle=Label(self.root,text="VACCINE REGISTRATION",bd=15,relief=RIDGE
                      ,bg="white",fg="darkgreen",font=("cavolini",20,"bold"),padx=2,pady=4)
        lbtitle.pack(side=TOP,fill=X)

        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=900,height=600)
        
        lblcomp=Label(DataFrame,text="Adhar Number:",font=("arial",20,"bold"),padx=100,pady=20)
        lblcomp.grid(row=1,column=0,sticky=W)
        txtcomp=Entry(DataFrame,width=29,font=("arial",15,"bold"))
        txtcomp.grid(row=1,column=1)

        lblcomp=Label(DataFrame,text="Name:",font=("arial",20,"bold"),padx=100,pady=20)
        lblcomp.grid(row=2,column=0,sticky=W)
        txtcomp=Entry(DataFrame,width=29,font=("arial",15,"bold"))
        txtcomp.grid(row=2,column=1)

        lblrefno=Label(DataFrame,text="Age:",font=("arial",20,"bold"),padx=100,pady=18)
        lblrefno.grid(row=3,column=0,sticky=W)
        ref_combo=ttk.Combobox(DataFrame,width=27,font=("arial",15,"bold"),state='readonly')
        ref_combo["values"]=("15-18","18 above")
        ref_combo.grid(row=3,column=1)
        ref_combo.current(0)

        lblgender = Label(root, text="Gender:",width=20,font=("arial",20,"bold"),padx=12)
        lblgender.place(x=4,y=380)
        var = IntVar()
        Radiobutton(root, text="Male",font=("arial",15,"bold"),padx =10, variable=var, value=1).place(x=500,y=380)
        Radiobutton(root, text="Female",font=("arial",15,"bold"),padx = 40, variable=var, value=2).place(x=600,y=380)

        lblrefno=Label(DataFrame,text="Vaccine type:",font=("arial",20,"bold"),padx=100,pady=90)
        lblrefno.grid(row=5,column=0,sticky=W)
        ref_combo=ttk.Combobox(DataFrame,width=27,font=("arial",15,"bold"),state='readonly')
        ref_combo["values"]=("Covaxin","Covishield")
        ref_combo.grid(row=5,column=1)
        ref_combo.current(0)


        btnLogin=Button(DataFrame,text="Submit",width=15,font=('arial',20,'bold'),padx=100,pady=10,bg='white',
                                    command=DataFrame)
        btnLogin.place(x=170,y=400)
        def __init__ (self):
            tkinter.messagebox.askyesno("Vaccine Registration", "You have been registered")
       
        


       

if __name__ =="__main__":
    root=Tk()
    obj=Vaccine(root)
    root.mainloop()
