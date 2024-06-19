from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Orphanage:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('ORPHANAGE MANAGEMENT SYSTEM')
        
        #variables
        self.var_member_id=StringVar()
        self.var_name=StringVar()
        self.var_admission_date=StringVar()
        self.var_date_of_birth=StringVar()
        self.var_age=StringVar()
        self.var_birthMark=StringVar()
        self.var_gender=StringVar()
        
        lbl_title=Label(self.root,text='ORPHANAGE MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',35,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #Main_frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        
        #Upper_frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Orphan Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        #Labels Entry
        #member id
        id=Label(upper_frame,text='Member ID:',font=('arial',11,'bold'),bg='white')
        id.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_member_id, width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text="Name:",bg='white')
        lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name ,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Admission Date
        lbl_admissionDate=Label(upper_frame,font=('arial',12,'bold'),text="Admission Date:",bg='white')
        lbl_admissionDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_admissionDate=ttk.Entry(upper_frame,textvariable=self.var_admission_date ,width=22,font=('arial',11,'bold'))
        txt_admissionDate.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Date Of Birth
        lbl_dateofBirth=Label(upper_frame,font=('arial',12,'bold'),text="Date Of Birth:",bg='white')
        lbl_dateofBirth.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateofBirth=ttk.Entry(upper_frame,textvariable=self.var_date_of_birth, width=22,font=('arial',11,'bold'))
        txt_dateofBirth.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #Age
        lbl_age=Label(upper_frame,font=('arial',12,'bold'),text="Age:",bg='white')
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age, width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #BirthMark
        lbl_birthMark=Label(upper_frame,font=('arial',12,'bold'),text="BirthMark:",bg='white')
        lbl_birthMark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthMark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('arial',11,'bold'))
        txt_birthMark.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        #Gender
        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text="Gender:",bg='white')
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        #Radio Button Gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender ,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender ,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #Add Button
        btn_add=Button(button_frame,command=self.add_data,text='Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #Update Button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,command=self.delete_data ,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_data, text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        # Background right side image
        img_crime=Image.open('background.jpeg')
        img_crime=img_crime.resize((470,245),Image.Resampling.LANCZOS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)

        #Down_frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Orphan Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search ,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Member_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search ,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_data, text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame, command=self.fetch_data, text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        agency=Label(search_frame,font=("arial",30,"bold"),text="SAI SRI ORPHANAGE",bg='white',fg='crimson')
        agency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.orphans_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.orphans_table.xview)
        scroll_y.config(command=self.orphans_table.yview)

        self.orphans_table.heading("1",text="Member Id")
        self.orphans_table.heading("2",text="Name")
        self.orphans_table.heading("3",text="Admission Date")
        self.orphans_table.heading("4",text="Date of Birth")
        self.orphans_table.heading("5",text="Age")
        self.orphans_table.heading("6",text="Birth Mark")
        self.orphans_table.heading("7",text="Gender")

        self.orphans_table['show']='headings'

        self.orphans_table.column("1",width=50)
        self.orphans_table.column("2",width=140)
        self.orphans_table.column("3",width=100)
        self.orphans_table.column("4",width=100)
        self.orphans_table.column("5",width=50)
        self.orphans_table.column("6",width=140)
        self.orphans_table.column("7",width=100)

        self.orphans_table.pack(fill=BOTH,expand=1)

        self.orphans_table.bind("<ButtonRelease>",self.get_cursor )
        self.fetch_data()

    # Add function

    def add_data(self):
        if self.var_member_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Ammu123!', database='dbcep')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into orphans values(%s,%s,%s,%s,%s,%s,%s)',(self.var_member_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_admission_date.get(),
                                                                                                            self.var_date_of_birth.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_birthMark.get(),
                                                                                                            self.var_gender.get(),))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('successful', 'record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    # fetch data

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='Ammu123!', database='dbcep')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from orphans')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.orphans_table.delete(*self.orphans_table.get_children())
            for i in data:
                self.orphans_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.orphans_table.focus()
        content=self.orphans_table.item(cursor_row)
        data=content['values']

        self.var_member_id.set(data[0])
        self.var_name.set(data[2])
        self.var_admission_date.set(data[4])
        self.var_date_of_birth.set(data[5])
        self.var_age.set(data[7])
        self.var_birthMark.set(data[9])
        self.var_gender.set(data[12])

    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('update', "Are you sure you want to update this record?")
                if update>0:
                    conn=mysql.connector.connect(host='localhost', username='root',password='Ammu123!', database='dbcep')
                    my_cursor=conn.cursor() 
                    my_cursor.execute('update orphans set name=%s, admission_date=%s, dateOfbirth=%s,  age=%s, BirthMark=%s, gender=%s, where member_id=%s',(
                                                                                                                self.var_name.get(),
                                                                                                                self.var_admission_date.get(),
                                                                                                                self.var_date_of_birth.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_birthMark.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_member_id.get()))    
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('successful', 'record has been updated')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')   
    
    #delete

    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                delete=messagebox.askyesno('Delete', "Are you sure you want to Delete this record?")
                if delete>0:
                    conn=mysql.connector.connect(host='localhost', username='root',password='Ammu123!', database='dbcep')
                    my_cursor=conn.cursor() 
                    sql="DELETE FROM orphans WHERE member_id= %s "
                    value=(self.var_member_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('successful', 'record has been deleted')
            except Exception as es:
                messagebox.showerror('error',f'Due to {str(es)}')   

    # clear

    def clear_data(self):
        self.var_member_id.set("")
        self.var_name.set("")
        self.var_admission_date.set("")
        self.var_date_of_birth.set("")
        self.var_age.set("")
        self.var_birthMark.set("")
        self.var_gender.set("")
    # search

    def search_data(self): 
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Ammu123!', database='dbcep')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from orphans where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.orphans_table.delete(*self.orphans_table.get_children())
                    for i in rows:
                        self.orphans_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 



if __name__=="__main__":
    root=Tk()
    obj=Orphanage(root)
    root.mainloop()

