from tkinter import *
import math,random,datetime
from tkinter import messagebox
import os
class Bill_App:
    def __init__(self):
        self.root=Tk()
        
        # m=root.maxsize()
        # self.root.geometry('{}x{}+0+0'.format(*m))
        self.root.geometry("1536x864+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"

        title=Label(self.root,text="Billing Software",bd=7,relief=GROOVE,bg=bg_color,fg="white",font="times 30 bold").pack(fill=X,pady=16)
        # ================ Variables ===============================================
        # -------------Cosmetic-------------------------
        self.bath_soap=IntVar()
        self.face_Cream=IntVar()
        self.face_Wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.body_loshan=IntVar()

        # ----------------Grocery--------------------------
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        # ---------------- Cold Drinks --------------------
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        # ---------------- Total Price and Tax ------------
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        # ----------------- Customer Price -----------------
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        # ================Customer Details Frame ===================================
        F1=LabelFrame(self.root,bd=7,relief=GROOVE,text="Customer Details",font="times 15 bold",fg="gold",bg=bg_color)
        F1.place(x=0,y=78,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font="times 18 bold",bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=10)
        cname_txt=Entry(F1,font="arial 15",textvariable=self.c_name,bd=3,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=20)

        cnum_lbl=Label(F1,text="Contact No.",font="times 18 bold",bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=10)
        cnum_txt=Entry(F1,font="arial 15",textvariable=self.c_phon,bd=3,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=10)
        
        cbill_lbl=Label(F1,text="Bill No",font="times 18 bold",bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=10)
        cbill_txt=Entry(F1,font="arial 15",textvariable=self.search_bill,bd=3,relief=SUNKEN).grid(row=0,column=5,padx=20,pady=10)
        
        bsearch_lbl=Button(F1,text="Search",command=self.find_bill,width=10,font="arial 12 bold",fg=bg_color,bg="cadetblue").grid(row=0,column=6,padx=10,pady=10)
        
        # ================Cosmetics Frame ===============================
        F2=LabelFrame(self.root,bd=7,relief=GROOVE,text="Cosmetics",font="times 15 bold",fg="gold",bg=bg_color)
        F2.place(x=5,y=185,width=360,height=400)

        bathsoap_lbl=Label(F2,text="Bath Soap",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        bathsoap_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.bath_soap,bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="W")

        facecream_lbl=Label(F2,text="Face Cream",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        facecream_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.face_Cream,bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="W")

        facewash_lbl=Label(F2,text="Face wash",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        facewash_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.face_Wash,bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="W")

        hairspray_lbl=Label(F2,text="Hair Spray",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="W")
        hairspray_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.spray,bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="W") 

        hairgel_lbl=Label(F2,text="Hair Gel",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="W")
        hairgel_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.gel,bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="W")

        bodyloshan_lbl=Label(F2,text="Body Loshan",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="W")
        bodyloshan_txt=Entry(F2,width=10,font="times 16 bold",textvariable=self.body_loshan,bd=3,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky="W") 

        # ================Grocery Frame ===============================
        F3=LabelFrame(self.root,bd=7,relief=GROOVE,text="Grocery",font="times 15 bold",fg="gold",bg=bg_color)
        F3.place(x=380,y=185,width=360,height=400)

        rice_lbl=Label(F3,text="Rice",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=20,pady=10,sticky="W")
        rice_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.rice,bd=3,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=10,sticky="W")

        oil_lbl=Label(F3,text="Food Oil",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=20,pady=10,sticky="W")
        oil_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.oil,bd=3,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=10,sticky="W")

        daal_lbl=Label(F3,text="Daal",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=20,pady=10,sticky="W")
        daal_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.daal,bd=3,relief=SUNKEN).grid(row=2,column=1,padx=20,pady=10,sticky="W")

        wheat_lbl=Label(F3,text="Wheat",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=20,pady=10,sticky="W")
        wheat_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.wheat,bd=3,relief=SUNKEN).grid(row=3,column=1,padx=20,pady=10,sticky="W")

        sugar=Label(F3,text="Sugar",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=20,pady=10,sticky="W")
        sugar_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.sugar,bd=3,relief=SUNKEN).grid(row=4,column=1,padx=20,pady=10,sticky="W")

        tea_lbl=Label(F3,text="Tea",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=20,pady=10,sticky="W")
        tea_txt=Entry(F3,width=10,font="times 16 bold",textvariable=self.tea,bd=3,relief=SUNKEN).grid(row=5,column=1,padx=20,pady=10,sticky="W")

        # ================Grocery Frame ===============================
        F4=LabelFrame(self.root,bd=7,relief=GROOVE,text="Cold Drinks",font="times 15 bold",fg="gold",bg=bg_color)
        F4.place(x=755,y=185,width=360,height=400)

        maza_lbl=Label(F4,text="Maza",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        maza_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.maza,bd=3,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="W")

        cock_lbl=Label(F4,text="Cock",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        cock_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.cock,bd=3,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="W")

        frooti_lbl=Label(F4,text="Frooti",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        frooti_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.frooti,bd=3,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="W")

        thumsup_lbl=Label(F4,text="Thumbs Up",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="W")
        thumsup_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.thumsup,bd=3,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="W") 

        limca_lbl=Label(F4,text="Limca",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="W")
        limca_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.limca,bd=3,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="W")

        sprit_lbl=Label(F4,text="Sprit",font="times 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="W")
        sprit_txt=Entry(F4,width=10,font="times 16 bold",textvariable=self.sprite,bd=3,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky="W")

        # ================ Bill Frame ============================================
        F5=Frame(self.root,bd=7,relief=GROOVE)
        F5.place(x=1120,y=185,width=383,height=400)

        b_title=Label(F5,text="Bill Area",bd=4,relief=GROOVE,font="times 15 bold").pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.welcome_bill()
        
        # ================== Billing Menu Frame ===================================
        F6=LabelFrame(self.root,bd=7,relief=GROOVE,text="Billing Menu",font="times 15 bold",fg="gold",bg=bg_color)
        F6.place(x=0,y=590,relwidth=1,height=197)

        totalCosm_lbl=Label(F6,text="Total Cosmetic Price",font="times 16 bold",bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="W")
        totalCOsm_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.cosmetic_price,bd=3,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=10,sticky="W")

        totalGroc_lbl=Label(F6,text="Total Grocery Price",font="times 16 bold",bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="W")
        totalGroc_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.grocery_price,bd=3,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=10,sticky="W")

        totalCold_lbl=Label(F6,text="Total Cold Drinks Price",font="times 16 bold",bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="W")
        totalCold_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.cold_drink_price,bd=3,relief=SUNKEN).grid(row=2,column=1,padx=20,pady=10,sticky="W")

        CosmTex_lbl=Label(F6,text="Cosmetic Tax",font="times 16 bold",bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=10,sticky="W")
        CosmTax_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.cosmetic_tax,bd=3,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=10,sticky="W")

        GrocTax_lbl=Label(F6,text="Grocery Tax",font="times 16 bold",bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=10,sticky="W")
        GrocTax_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.grocery_tax,bd=3,relief=SUNKEN).grid(row=1,column=3,padx=20,pady=10,sticky="W")

        ColdTax_lbl=Label(F6,text="Cold Drink Tax",font="times 16 bold",bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=10,sticky="W")
        ColdTax_txt=Entry(F6,width=15,font="times 16 bold",textvariable=self.cold_drink_tax,bd=3,relief=SUNKEN).grid(row=2,column=3,padx=20,pady=10,sticky="W")

        # ================ Button Frame ============================
        F7=Frame(F6,bd=7,relief=GROOVE,)
        F7.place(x=840,y=10,width=660,height=138)
        btn_total=Button(F7,text="Total",width=11,bd=5,pady=20,bg="cadetblue",font="areal 15 bold",command=self.total).grid(row=1,column=0,padx=5,pady=20)
        btn_biGen=Button(F7,text="Generate Bill",width=11,bd=5,pady=20,bg="cadetblue",font="areal 15 bold",command=self.bill_area).grid(row=1,column=1,padx=5,pady=20)
        btn_clear=Button(F7,text="Clear",width=11,bd=5,pady=20,bg="cadetblue",font="areal 15 bold",command=self.clear).grid(row=1,column=2,padx=5,pady=20)
        btn_exit=Button(F7,text="Logout",width=11,bd=5,pady=20,bg="cadetblue",font="areal 15 bold",command=self.logout).grid(row=1,column=3,padx=5,pady=20)
        
        # ======================== Calculation Field ===================

    def total(self):
        # ----------Cosmetic Total -------------
        self.sop=self.bath_soap.get()*40
        self.cream=self.face_Cream.get()*180
        self.fewash=self.face_Wash.get()*60
        self.spr=self.spray.get()*190
        self.gell=self.gel.get()*140
        self.loshan=self.body_loshan.get()*180

        self.total_cosmetic_price = float(
                                            self.sop+
                                            self.cream+
                                            self.fewash+
                                            self.spr+
                                            self.gell+
                                            self.loshan
                                            )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        # ---------------Grocery Total --------------------
        self.rice1=self.rice.get()*40
        self.oil1=self.oil.get()*120
        self.daal1=self.daal.get()*80
        self.wheat1=self.wheat.get()*30
        self.sugar1=self.sugar.get()*40
        self.tea1=self.tea.get()*180

        self.total_grocery_price = float(
                                            self.rice1+
                                            self.oil1+
                                            self.daal1+
                                            self.wheat1+
                                            self.sugar1+
                                            self.tea1         
                                            )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        # ----------------- Cold Drink -----------------------
        self.maza1=self.maza.get()*40
        self.cock1=self.cock.get()*38
        self.frooti1=self.frooti.get()*20
        self.thumsup1=self.thumsup.get()*45
        self.limca1=self.limca.get()*25
        self.sprite1=self.sprite.get()*35

        self.total_cold_price = float(
                                       self.maza1+
                                       self.cock1+
                                       self.frooti1+
                                       self.thumsup1+
                                       self.limca1+
                                       self.sprite1
                                    )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_price))
        self.col_tax=round((self.total_cold_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.col_tax))

        self.total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_cold_price +
                                self.c_tax +
                                self.g_tax + 
                                self.col_tax
                                )

    def welcome_bill(self):
        cdt = datetime.datetime.now()
        self.d=str(cdt.strftime("%Y-%m-%d  %a,%I:%M:%S %p"))
        # print(self.d)
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t Welcome in WEBCODE Retails\n")
        self.txtarea.insert(END,"\t     Mobile : 79*****291\n")
        self.txtarea.insert(END,f"\n \t\t{self.d}")
        self.txtarea.insert(END,f"\n Bill Number   : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number  : {self.c_phon.get()}")
        self.txtarea.insert(END,"\n ==========================================")
        self.txtarea.insert(END,"\n Products\t\tQTY \t\tPrice")
        self.txtarea.insert(END,"\n ==========================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details is Required")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","Products is not selected")
        else:
            self.welcome_bill()
            # =================== Cosmetic ===================================
            if self.bath_soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.bath_soap.get()} \t\t{self.sop}")
            if self.face_Cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_Cream.get()} \t\t{self.cream}")
            if self.face_Wash.get()!=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.face_Wash.get()} \t\t{self.fewash}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()} \t\t{self.spr}")
            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gel.get()} \t\t{self.gell}")
            if self.body_loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.body_loshan.get()} \t\t{self.loshan}")
            
            # =================== Grocery ===================================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()} \t\t{self.rice1}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.oil.get()} \t\t{self.oil1}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()} \t\t{self.daal1}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()} \t\t{self.wheat1}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()} \t\t{self.sugar1}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()} \t\t{self.tea1}")
            
            # =================== Cold_Drink ===================================
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()} \t\t{self.maza1}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()} \t\t{self.cock1}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()} \t\t{self.frooti1}")
            if self.thumsup.get()!=0:
                self.txtarea.insert(END,f"\n Thums Up\t\t{self.thumsup.get()} \t\t{self.thumsup1}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()} \t\t{self.limca1}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()} \t\t{self.sprite1}")
            
            self.txtarea.insert(END,"\n ------------------------------------------")

            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t: {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t: {self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t: {self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t: Rs. {self.total_bill}")
            self.txtarea.insert(END,"\n ------------------------------------------")
            self.save_bill()
        
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you Want save bill?")
        if op>0:
            self.bill_data=self.txtarea.get('0.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved Successfully!!")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.")

    def clear(self):
        op = messagebox.askyesno("Clear","Do you Really want to Clear")
        if op>0:                
            # -------------Cosmetic-------------------------
            self.bath_soap.set(0)
            self.face_Cream.set(0)
            self.face_Wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.body_loshan.set(0)

            # ----------------Grocery--------------------------
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ---------------- Cold Drinks --------------------
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
        
        # ---------------- Total Price and Tax ------------
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # ----------------- Customer Price -----------------
        self.c_name.set("")
        self.c_phon.set("")
        self.search_bill.set("")
        self.welcome_bill()

    def logout(self):
        op = messagebox.askyesno("Exit","Do you Really want to Logout")
        if op>0:
            self.root.destroy()
        import login

#root=Tk()
#ob=Bill_App(root)  
#root.mainloop()