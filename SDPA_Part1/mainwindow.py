import tkinter as tk
import tkinter.messagebox
import car_rental as car

NewCars=car.Carsshop()
NewCustomer=car.Customer()
NewVIP=car.VIP()

window = tk.Tk()
window.title('Car Rental System')
window.geometry('500x300')
window.resizable(width=False, height=False)

# LABLE
lab_title = tk.Label(window, text='THIS IS A CAR RENTAL SYSTEM', bg='YELLOW', font=('Arial', 20), width=100, height=2)
lab_title.pack()
l1 = tk.Label(window, text='rent', bg='green')
l2 = tk.Label(window, text='return', bg='green')



# mainfunction
def hit_rent():
    def do_rent():
        carname=''
        select_car = var.get()
        if select_car=='1':
            carname='Hatchback'
        elif select_car=='2':
            carname = 'Sedan'
        elif select_car=='3':
            carname= 'SUV'
        select_day = s_rentday.get()

        if (select_car=='1' and NewCars.num_hatchback>=1) or (select_car=='2' and NewCars.num_sedan>=1) or (select_car=='3' and NewCars.num_suv>=1):
            NewCars.rent_car(select_car)
            if NewVIP.isVIP==0:
                FEE = NewCustomer.fee(select_car,select_day)
                NewCustomer.add_carrent(NewCustomer.customer,select_car,FEE,select_day)
            else :
                FEE =NewVIP.discount(select_car,select_day)
                NewVIP.add_carrent(NewCustomer.customer,select_car,FEE,select_day)
            INFO = 'You have rented a {} car for {} days. You will be charged {} pounds'.format(carname,select_day,FEE)

            is_rent = tkinter.messagebox.askokcancel(title='Rent Confirm', message=INFO)

            if is_rent:
                    tkinter.messagebox.showinfo(title='RENT SECCESS',
                                            message='Congratulations on your successful car rental！We hope that you enjoy our service.')

                    window_rent.destroy()
        elif select_car=='':
            tkinter.messagebox.showerror(title='Rent Error', message='Incorrect input information')
        else:
            tkinter.messagebox.showerror(title='Rent Error', message='The car you selected is out of stock')
#rentwindow
    if NewCustomer.customer == '':
        tkinter.messagebox.showerror(title='Rent Error', message='Please select customer account')
    else:

        infolist = NewCustomer.df_win[NewCustomer.df_win.CNAME == NewCustomer.customer]
        if infolist.empty:
            window_rent = tk.Toplevel(window)
            window_rent.geometry('500x350')
            window_rent.title('rent window')
            window_rent.resizable(width=False, height=False)
            lab_renttitle = tk.Label(window_rent, text='RENT A CAR', bg='YELLOW', font=('Arial', 20), width=100,
                         height=2)
            lab_renttitle.pack()
            frame = tk.Frame(window_rent)
            frame.pack()
            frame_1 = tk.Frame(frame)
            frame_2 = tk.Frame(frame)
            frame_1.pack(side='left')
            frame_2.pack(side='right')
            tk.Label(frame_1, text='Hatchback', bg='grey',width=30).pack()
            tk.Label(frame_1, text='sedan', bg='grey',width=30).pack()
            tk.Label(frame_1, text='SUV', bg='grey',width=30).pack()
            num_1=NewCars.num_hatchback
            num_2=NewCars.num_sedan
            num_3=NewCars.num_suv
            tk.Label(frame_2, text=num_1, bg='green',width=30).pack()
            tk.Label(frame_2, text=num_2, bg='green',width=30).pack()
            tk.Label(frame_2, text=num_3, bg='green',width=30).pack()
            lab_rentcartype=tk.Label(window_rent, text='Car Type:', font=('Arial', 15), width=100,
                         height=2)
            lab_rentcartype.place(x=-400, y=120)
            var = tk.StringVar()
            r1 = tk.Radiobutton(window_rent, text='Hatchback ',  variable=var, value='1')
            r2 = tk.Radiobutton(window_rent, text='Sedan      ', variable=var, value='2')
            r3 = tk.Radiobutton(window_rent, text='SUV        ', variable=var, value='3')

            r1.place(x=130, y=125, anchor='nw')
            r2.place(x=130, y=150, anchor='nw')
            r3.place(x=130, y=175, anchor='nw')
            lab_renttime = tk.Label(window_rent, text='Rent Time(Day):', font=('Arial', 15), width=100,
                               height=2)
            lab_renttime.place(x=-380, y=200)

            s_rentday = tk.Scale(window_rent, from_=1, to=60, orient=tk.HORIZONTAL, length=300, showvalue=1, tickinterval=7,
                 resolution=1)
            s_rentday.place(x=130, y=200, anchor='nw')
            btn_comfirm_rent = tk.Button(window_rent, text='rent now', bg="blue", font=('Arial', 20), width=8, height=2,
                                 command=do_rent)
            btn_comfirm_rent.place(x=180, y=280, anchor='nw')
        else:
            is_return = tkinter.messagebox.askokcancel(title='Rent Confirm', message="The customer has already rented a car. Will you return it first")
            if is_return:
                hit_return()

def hit_return():
    if NewCustomer.customer == '':
        tkinter.messagebox.showerror(title='Return Error', message='Please select customer account')
    else:
        infolist = NewCustomer.df_win[NewCustomer.df_win.CNAME == NewCustomer.customer]
        if infolist.empty:
            tkinter.messagebox.showerror(title='Return Error', message='The customer did not rent the car')
        else:
            a=infolist.index.tolist()
            print(a)
            carname = ''
            select_car = infolist.iat[0, 1]
            FEE=infolist.iat[0,2]
            NewCustomer.df_win.drop(a[0], inplace=True)
            NewCars.return_car(select_car)
            if select_car == '1':
                carname = 'Hatchback'
            elif select_car == '2':
                carname = 'Sedan'
            elif select_car == '3':
                carname = 'SUV'

            Message_return='You have successfully returned a {} car, the total cost is {}.'.format(carname,FEE)
            tkinter.messagebox.showinfo(title='RENT SECCESS', message=Message_return)

#menu for customer

def do_job():
    NewCustomer.customer=var_cus.get()

def do_job2():
    if var_VIP.get()==1:
     NewVIP.isVIP =1


var_cus = tk.IntVar()
var_VIP = tk.IntVar()
menubar = tk.Menu(window)
Cusomermenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Customer', menu=Cusomermenu)
Cusomermenu.add_radiobutton(label='Customer0', command=do_job,value=0,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer1', command=do_job,value=1,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer2', command=do_job,value=2,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer3', command=do_job,value=3,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer4', command=do_job,value=4,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer5', command=do_job,value=5,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer6', command=do_job,value=6,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer7', command=do_job,value=7,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer8', command=do_job,value=8,variable=var_cus)
Cusomermenu.add_radiobutton(label='Customer9', command=do_job,value=9,variable=var_cus)
VIPmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='VIP', menu=VIPmenu)
VIPmenu.add_radiobutton(label='NO', command=do_job2,value=0,variable=var_VIP)
VIPmenu.add_radiobutton(label='YES', command=do_job2,value=1,variable=var_VIP)

window.config(menu=menubar)
#main function btn
btn_rent = tk.Button(window, text='RENT', bg="blue", font=('Arial', 20), width=10, height=5, command=hit_rent)
btn_rent.place(x=50, y=100, anchor='nw')
btn_return = tk.Button(window, text='RETURN', bg='blue', font=('Arial', 20), width=10, height=5, command=hit_return)
btn_return.place(x=300, y=100, anchor='nw')