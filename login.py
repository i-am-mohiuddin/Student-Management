from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Allen Management")
        self.root.geometry("1350x700+0+15")
        #-------------------All Images-------------
        self.bg_icon=ImageTk.PhotoImage(file="project/862737.png")
        self.user_icon=PhotoImage(file="project/21104.png")
        self.logo_icon=PhotoImage(file="project/unnamed.png")
        self.pass_icon=PhotoImage(file="project/lock.png")

        
        bg=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Allen Management System",font=("times",35,"italic bold"),bg="navy",fore="cyan",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        lo=Label(Login_Frame,text="Login Here",font=("times",20,"italic bold"),bg="white",fg="#08A3D2")
        lo.place(x=20,y=30)

        logo=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        user=Label(Login_Frame,text="User Name",image=self.user_icon,compound=LEFT,bg="white",font=("times",20,"italic bold")).grid(row=1,column=0,padx=20,pady=10)
        Password=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,bg="white",font=("times",20,"italic bold")).grid(row=2,column=0,padx=20,pady=10)
        
        #------------------variables----------------
        # self.uname=StringVar()
        # self.pass_=StringVar()
        
        self.userentry=Entry(Login_Frame,bd=5,relief=GROOVE,font=("times",15,"italic bold"))
        self.userentry.grid(row=1,column=1,padx=20)
        self.passentry=Entry(Login_Frame,bd=5,relief=GROOVE,font=("times",15,"italic bold"))
        self.passentry.grid(row=2,column=1,padx=20)

        loginbutt=Button(Login_Frame,text="Login",width=15,font=("times",15,"italic bold"),relief=RIDGE,bd=5,bg="cyan4",activebackground="green",activeforeground="blue",command=self.login).grid(row=3,column=1,pady=10)

        newacc=Button(Login_Frame,text="Requierd New Account ?",width=20,font=("times",12,"italic"),bg="white",borderwidth=0,fg="#b00857",command=self.new_acc)
        newacc.place(x=35,y=335)

    def manage(self):
        self.root.destroy()
        import dbms
    
    def new_acc(self):
        self.root.destroy()
        import regester
  
    def login(self):
        
        Host="localhost"
        User="root"
        Password="Mohiuddin@#8299"


        if self.userentry.get()=="" or self.passentry.get()=="":
            messagebox.showerror("Error","All Feilds are Required!!",parent=self.root)
        else:
            try:
                con=pymysql.connect(host=Host,user=User,password=Password,port=3307)
                mycursor=con.cursor()
                strr="use Management"
                mycursor.execute(strr)
                strr="select * from faculty where Email=%s and Password=%s"
                mycursor.execute(strr,(self.userentry.get(),self.passentry.get()))
                data=mycursor.fetchone()

                if data==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Login Successfully",parent=self.root)
                    self.login()
                



            except Exception as es:
                messagebox.showerror("Error"f"Error Due to: {str(es)}",parent=self.root)
        
        

root=Tk()
obj=Login_system(root)
root.mainloop()