from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import time
import os


class emplyee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x750")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee Payroll Mnagement System", font=("times new roman", 30, "bold"),
                      bg="#ADD8E6", fg="black").place(x=0, y=0, relwidth=1)
        all_employees_btn = Button(self.root, text="All Employees", command=self.employee_frame,
                                   font=("times new roman", 14), bg="#f0f0f0", fg="black", relief=SOLID)
        all_employees_btn.place(x=1100, y=10)
        # .....................frame1.................

        # ...........variables....................
        self.var_code = IntVar()
        self.var_desig = StringVar()
        self.var_dob = StringVar()
        self.var_name = StringVar()
        self.var_doj = StringVar()
        self.var_exp = StringVar()
        self.var_age = StringVar()
        self.var_proof = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        Frame1 = Frame(self.root, bd=4, relief=RIDGE)
        Frame1.place(x=10, y=60, width=750, height=580)
        Frame1.config(bg="white")
        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20,), bg="lightgray",
                       fg="black").place(x=0, y=0, relwidth=1)

        # ................row1...........
        lbl_code = Label(Frame1, text="Employee code", font=("times new roman", 18,), bg="white", fg="black").place(
            x=10, y=60)
        txt_code = Entry(Frame1, font=("times new roman", 18,), textvariable=self.var_code, bg="white",
                         fg="black").place(x=200, y=60, width=200)
        lbl_code = Button(Frame1, text="Search", font=("times new roman", 14), command=self.search, bg="#f0f0f0",
                          fg="black", relief=SOLID).place(x=420, y=60)

        # ................row2...........
        lbl_Designation = Label(Frame1, text="Designation", font=("times new roman", 18,), bg="white",
                                fg="black").place(x=10, y=120)
        txt_Designation = Entry(Frame1, font=("times new roman", 18,), textvariable=self.var_desig, bg="white",
                                fg="black").place(x=200, y=120, width=200)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 18,), bg="white", fg="black").place(x=420, y=120)
        txt_dob = Entry(Frame1, font=("times new roman", 18,), textvariable=self.var_dob, bg="white", fg="black").place(
            x=510, y=120, width=200)

        # ................row3...........
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=180)
        txt_name = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_name, bg="white",
                         fg="black").place(x=200, y=180, width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=180)
        txt_doj = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_doj, bg="white", fg="black").place(
            x=510, y=180, width=200)

        # ................row4...........
        lbl_Experience = Label(Frame1, text="Experience", font=("times new roman", 18), bg="white", fg="black").place(
            x=10, y=240)
        txt_Experience = Entry(Frame1, font=("times new roman", 18), bg="white", textvariable=self.var_exp,
                               fg="black").place(x=200, y=240, width=200)

        lbl_Age = Label(Frame1, text="Age", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=240)
        txt_Age = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_age, bg="white", fg="black").place(
            x=510, y=240, width=200)

        # ................row5...........
        lbl_Proof = Label(Frame1, text="Proof  ID", font=("times new roman", 18), bg="white", fg="black").place(x=10,
                                                                                                                y=300)
        txt_Proof = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_proof, bg="white",
                          fg="black").place(x=200, y=300, width=200)

        lbl_Gender = Label(Frame1, text="Gender", font=("times new roman", 18), bg="white", fg="black").place(x=420,
                                                                                                              y=300)
        txt_gend = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_gender, bg="white",
                         fg="black").place(x=510, y=300, width=200)

        # ................row6...........
        lbl_Email = Label(Frame1, text="Email", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=360)
        txt_Email = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_email, bg="white",
                          fg="black").place(x=200, y=360, width=200)

        lbl_con = Label(Frame1, text="Contact", font=("times new roman", 18), bg="white", fg="black").place(x=420,
                                                                                                            y=360)
        txt_con = Entry(Frame1, font=("times new roman", 18), textvariable=self.var_contact, bg="white",
                        fg="black").place(x=510, y=360, width=200)
        # ................row7...........
        lbl_Address = Label(Frame1, text="Address", font=("times new roman", 18), bg="white", fg="black").place(x=10,
                                                                                                                y=420)
        self.txt_Address = Text(Frame1, font=("times new roman", 18), bg="white", fg="black", height=4, width=42)
        self.txt_Address.place(x=200, y=420)

        # .....................frame2.................
        # ......................variables

        self.var_base_pay = StringVar()
        self.var_present = StringVar()
        self.var_medical = StringVar()
        self.var_conv = StringVar()
        self.var_p_f = StringVar()
        self.var_net_sal = StringVar()
        Frame2 = Frame(self.root, bd=4, relief=RIDGE)
        Frame2.place(x=770, y=60, width=490, height=300)
        Frame2.config(bg="white")
        title2 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20,), bg="lightgray",
                       fg="black").place(x=0, y=0, relwidth=1)

        
        # .............row1...........
        lbl_Base = Label(Frame2, text="Base Pay", font=("times new roman", 18,), bg="white", fg="black").place(x=5,
                                                                                                               y=60)
        txt_Base = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_base_pay, bg="white",
                         fg="black").place(x=120, y=60, width=90)

        lbl_Present = Label(Frame2, text="Base Days", font=("times new roman", 18,), bg="white", fg="black").place(
            x=230, y=60)
        txt_Present = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_present, bg="white",
                            fg="black").place(x=370, y=60, width=90)

        # .............row2...........
        lbl_Medical = Label(Frame2, text="Medical", font=("times new roman", 18,), bg="white", fg="black").place(x=5,
                                                                                                                 y=120)
        txt_Medical = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_medical, bg="white",
                            fg="black").place(x=120, y=120, width=90)

        lbl_Convinence = Label(Frame2, text="Convinence", font=("times new roman", 18,), bg="white", fg="black").place(
            x=230, y=120)
        txt_Convinence = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_conv, bg="white",
                               fg="black").place(x=370, y=120, width=90)

        # .............row3...........
        lbl_PF = Label(Frame2, text="P.F", font=("times new roman", 18,), bg="white", fg="black").place(x=5, y=180)
        txt_PF = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_p_f, bg="white", fg="black").place(
            x=120, y=180, width=90)

        lbl_net = Label(Frame2, text="Net Salary", font=("times new roman", 18,), bg="white", fg="black").place(x=230,
                                                                                                                y=180)
        txt_net = Entry(Frame2, font=("times new roman", 18), textvariable=self.var_net_sal, bg="white",
                        fg="black").place(x=370, y=180, width=90)

        # ..............adding buttons ..............

        btn_Calculate = Button(Frame2, text="Calculate", font=("times new roman", 14), command=self.calculate,
                               bg="#f0f0f0", fg="black", relief=SOLID).place(x=180, y=240)
        btn_Save = Button(Frame2, text="Save", font=("times new roman", 14), command=self.add, bg="#f0f0f0", fg="black",
                          relief=SOLID, ).place(x=280, y=240)
        btn_clear = Button(Frame2, text="Clear", command=self.clear, font=("times new roman", 14), bg="#f0f0f0",
                           fg="black", relief=SOLID).place(x=350, y=240)
        # lbl_code = Button(Frame2,text="Print",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID).place(x=360,y=240)

        # .....................Frame3.................
        Frame3 = Frame(self.root, bd=4, relief=RIDGE)
        Frame3.place(x=770, y=370, width=490, height=270)
        Frame3.config(bg="white")

        # .....calculator frame
        cal_frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        cal_frame.place(x=5, y=5, width=216, height=255)

        self.var_txt = StringVar()
        self.var_operator = ''

        def btn_click(num):
            self.var_operator += str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def clr():
            self.var_operator = ''
            self.var_txt.set(self.var_operator)

        title4 = Entry(cal_frame, text="Calculator", textvariable=self.var_txt, font=("times new roman", 20,),
                       bg="lightgray", fg="black").place(x=0, y=0, relwidth=1)

        # .................calculator row 1 ...............
        btn7 = Button(cal_frame, text="7", command=lambda: btn_click(7), font=("times new roman ", 15, "bold")).place(
            x=2, y=42, width=50, height=40)
        btn8 = Button(cal_frame, text="8", command=lambda: btn_click(8), font=("times new roman ", 15, "bold")).place(
            x=55, y=42, width=50, height=40)
        btn9 = Button(cal_frame, text="9", command=lambda: btn_click(9), font=("times new roman ", 15, "bold")).place(
            x=108, y=42, width=50, height=40)
        btn_div = Button(cal_frame, text="/", command=lambda: btn_click('/'),
                         font=("times new roman ", 15, "bold")).place(x=160, y=42, width=50, height=40)

        # .................calculator row 2 ...............
        btn4 = Button(cal_frame, text="4", command=lambda: btn_click(4), font=("times new roman ", 15, "bold")).place(
            x=2, y=86, width=50, height=40)
        btn5 = Button(cal_frame, text="5", command=lambda: btn_click(5), font=("times new roman ", 15, "bold")).place(
            x=55, y=86, width=50, height=40)
        btn6 = Button(cal_frame, text="6", command=lambda: btn_click(6), font=("times new roman ", 15, "bold")).place(
            x=108, y=86, width=50, height=40)
        btn_mul = Button(cal_frame, text="*", command=lambda: btn_click('*'),
                         font=("times new roman ", 15, "bold")).place(x=160, y=86, width=50, height=40)

        # # .................calculator row 3 ...............
        btn1 = Button(cal_frame, text="1", command=lambda: btn_click(1), font=("times new roman ", 15, "bold")).place(
            x=2, y=130, width=50, height=40)
        btn2 = Button(cal_frame, text="2", command=lambda: btn_click(2), font=("times new roman ", 15, "bold")).place(
            x=55, y=130, width=50, height=40)
        btn3 = Button(cal_frame, text="3", command=lambda: btn_click(3), font=("times new roman ", 15, "bold")).place(
            x=108, y=130, width=50, height=40)
        btn_plus = Button(cal_frame, text="+", command=lambda: btn_click('+'),
                          font=("times new roman ", 15, "bold")).place(x=160, y=130, width=50, height=40)

        # # .................calculator row 4 ...............
        btn0 = Button(cal_frame, text="0", command=lambda: btn_click(0), font=("times new roman ", 15, "bold")).place(
            x=2, y=174, width=50, height=40)
        btn_neg = Button(cal_frame, text="-", command=lambda: btn_click('-'),
                         font=("times new roman ", 15, "bold")).place(x=55, y=174, width=50, height=40)
        btn_dot = Button(cal_frame, text=".", command=lambda: btn_click('.'),
                         font=("times new roman ", 15, "bold")).place(x=108, y=174, width=50, height=40)
        btn_equal = Button(cal_frame, text="=", command=lambda: result(), font=("times new roman ", 15, "bold")).place(
            x=160, y=174, width=50, height=40)

        btn_clr = Button(cal_frame, text="Clear", command=lambda: clr(), font=("times new roman ", 15, "bold")).place(
            x=80, y=215, width=60, height=35)

        sal_frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_frame.place(x=225, y=5, width=253, height=255)
        title5 = Label(sal_frame, text="Salary Slip", font=("times new roman", 20,), bg="lightgray", fg="black").place(
            x=0, y=0, relwidth=1)

        sal_frame2 = Frame(sal_frame, bg="white", bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=32, relwidth=1, height=180)
        lbl_print = Button(sal_frame, text="Save", command=self.save_record, font=("times new roman", 14), bg="#f0f0f0",
                           fg="black", relief=SOLID, ).place(x=100, y=215, width=60, height=35)
        sample = f'''Company Name: BVP, Vasai (w)\n
Address: Xyz, Floor4
..........................................................
Employee ID\t\t: 1024
Generated On\t\t: 20-12-2020

..........................................................
Total Present\t\t: 20
Convinence\t\t: Rs.1000
Medical\t\t: Rs.2000
PF\t\t: Rs.1500
..........................................................
Net Salary\t\t: Rs.25455222 \n\n
This is a computer-generated slip, not requiring any signature
'''

        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        self.txt_salary_slip = Text(sal_frame2, font=("times new roman", 13), bg="#f0f0f0", fg="black",
                                    yscrollcommand=scroll_y.set)
        self.txt_salary_slip.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_slip.yview)
        self.txt_salary_slip.insert(END, sample)

        # self.check_conn()

    #  .............................Adding entry to database .....................................
    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="empoyee")
            cur = conn.cursor()
            cur.execute("SELECT * FROM emp WHERE e_id = %s", (self.var_code.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Employee ID,\n try with valid Employee ID")
            else:
                print(row)
                self.var_code.set(row[0]), self.var_desig.set(row[1]), self.var_name.set(row[2]), self.var_doj.set(
                    row[3]),
                self.var_exp.set(row[4]), self.var_age.set(row[5]), self.var_proof.set(row[6]),
                self.var_gender.set(row[7]),
                self.var_email.set(row[8]), self.var_contact.set(row[9]), self.txt_Address.delete('1.0', END)
                self.txt_Address.insert(END, row[10])
                self.var_base_pay.set(row[11]), self.var_present.set(row[12]), self.var_medical.set(row[13]),
                self.var_conv.set(row[14]), self.var_p_f.set(row[15])
                self.var_net_sal.set(row[16])
                file_ = open('salary_receipt/' + str(row[17]), 'r')
                self.txt_salary_recipt.delete('1.0', END)
                for i in file_:
                    self.txt_salary_recipt.insert(END, i)
                file_.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred due to {ex}")

            # ...................adding to db................

    def add(self):
        if self.var_code.get() == '' or self.var_base_pay.get() == '':
            messagebox.showerror("Error", "All Fields Are Required")
            return
        if self.var_code.get() < 0:
            messagebox.showerror("Error", "Employee code cannot be negative ")
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="empoyee")
            cur = conn.cursor()
            cur.execute("SELECT * FROM emp WHERE e_id = %s", (self.var_code.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Employee ID already available")
            else:
                cur.execute(
                    "INSERT INTO emp(e_id,Designation,Name,doj,Experience,Age,Proof,Gender,Email,Contact,Address,Base_Pay,Base_Days,Medical,Convinence,P_F,Net_Salary,reciept) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
                    (self.var_code.get(), self.var_desig.get(), self.var_name.get(), self.var_doj.get(),
                     self.var_exp.get(), self.var_age.get(), self.var_proof.get(),
                     self.var_gender.get(),
                     self.var_email.get(), self.var_contact.get(), self.txt_Address.get(1.0, 'end-1c'),
                         self.var_base_pay.get(), self.var_present.get(), self.var_medical.get(),
                     self.var_conv.get(), self.var_p_f.get(), self.var_net_sal.get(), "reciept"))

                # cur.execute("INSERT INTO emp_salary(e_id,Designation,Name,doj,Experience,Age,Proof,Gender,Email,Contact,Address,Base_Pay,Base_Days,Medical,Convinence,P_F,Net_Salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)",
                #             (self.var_code.get(), self.var_desig.get(), self.var_name.get(), self.var_doj.get(),
                #             self.var_exp.get(), self.var_age.get(), self.var_proof.get(), self.var_gender.get(),
                #             self.var_email.get(), self.var_contact.get(),  self.txt_Address.get(1.0, 'end-1c'),
                #             self.var_base_pay.get(), self.var_present.get(), self.var_medical.get(),
                #             self.var_conv.get(), self.var_p_f.get(), self.var_net_sal.get()))
                messagebox.showinfo("Success", "Record Added Successfully")

                conn.commit()
                conn.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred due to {ex}")
            # /////////////////saving recoed//////////////////

    def save_record(self):
        try:
            directory = 'salary_receipt'
            if not os.path.exists(directory):
                os.makedirs(directory)

            file_path = os.path.join(directory, f"{self.var_code.get()}.txt")
            with open(file_path, 'w') as file_:
                # Use get() method to retrieve the content of the Text widget
                file_.write(self.txt_salary_slip.get('1.0', END))

            messagebox.showinfo("Success", "Record Added Successfully")

        except Exception as ex:
            messagebox.showerror("Error", f"Failed to save record: {ex}")

    def calculate(self):
        if self.var_base_pay.get() == '' or self.var_present.get() == '' or self.var_medical.get() == '' or self.var_conv.get() == '' or self.var_p_f.get() == '':
            messagebox.showerror(" Error", "All fields required")
        else:
            base_pay = int(self.var_base_pay.get())
            base_days = int(self.var_present.get())
            medical = int(self.var_medical.get())
            conv = int(self.var_conv.get())
            p_f = int(self.var_p_f.get())

            # Perform the calculation
            net_salary = base_pay * base_days + medical + conv - p_f

            # Update the net salary entry field
            self.var_net_sal.set(net_salary)
            new_sample = f'''Snowil & co: XYZ\n
Address: BVP, Vasai (w)
..........................................................
Employee ID\t\t: {self.var_code.get()}

Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}

..........................................................
Total Present\t\t: {self.var_present.get()}
Convinence\t\t: {self.var_conv.get()}
Medical\t\t: {self.var_medical.get()}
PF\t\t: {self.var_p_f.get()}
..........................................................

Net Salary\t: {self.var_net_sal.get()}

This is a computer-generated slip, not requiring any signature
          
'''
            self.txt_salary_slip.delete('1.0', END)
            self.txt_salary_slip.insert(END, new_sample)

            # ............clear valuing...............

    def clear(self):
        self.var_code.set(''), self.var_desig.set(''), self.var_name.set(''), self.var_doj.set(''),
        self.var_exp.set(''), self.var_age.set(''), self.var_proof.set(''),
        self.var_gender.set(''),
        self.var_email.set(''), self.var_contact.set(''),
        self.var_base_pay.set(''), self.var_present.set(''), self.var_medical.set(''),
        self.var_conv.set(''), self.var_p_f.set(''), self.var_net_sal.set('')

    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Management System ")
        self.root2.geometry("900x500+100+60")
        title = Label(self.root2, text="All Employee Record", font=("times new roman", 30, "bold"), bg="#ADD8E6",
                      fg="black").place(x=0, y=0, relwidth=1)

        self.root2.config(bg="white")
        self.root2.mainloop()


root = Tk()
obj = emplyee(root)
root.mainloop()
