import pandas as pd

class Carsshop:
    """definition of carsshop for manage the number of the car"""
    def __init__(self):
        """initialise the number of the cars"""
        self.num_hatchback=4
        self.num_sedan=3
        self.num_suv = 3


    def rent_car(self,kind_car):
        """rent the car according to the type of car to reduce the corresponding car"""
        if int(kind_car) == 1 and self.num_hatchback>0:
           self.num_hatchback-=1
           return 1
        elif int(kind_car)== 2 and self.num_sedan>0:
           self.num_sedan -= 1
           return 1
        elif int(kind_car) == 3 and self.num_suv>0:
           self.num_suv -= 1
           return 1
        else:
            raise ValueError("input error")



    def return_car(self,kind_car):
        """return the car, increase the car according to the type of car"""
        if kind_car == 1 :
            self.num_suv += 1
        elif kind_car == 2 :
            self.num_hatchback += 1
        elif kind_car == 3 :
            self.num_sedan += 1



class Customer():
    """definition of customer for manage the message of the renting"""
    def __init__(self):
        self.df = pd.DataFrame(columns=['ORDER_ID', 'cartype', 'fee', 'days','isVIP'])
        self.cid=0
        """ for mainwindow """
        self.customer = ''
        self.cName = ''
        self.df_win = pd.DataFrame(columns=['CNAME', 'cartype', 'fee', 'days'])

    def fee(self,kind_car,rent_time):
        """Calculate the cost of the average user """
        if int(rent_time) <= 7 and int(rent_time)> 0 :
            if int(kind_car) == 1:
                fee = rent_time * 30
            elif int(kind_car) == 2:
                fee = rent_time * 50
            elif int(kind_car) == 3:
                fee = rent_time * 100
            else:
                raise ValueError("rent_car error")
            return fee
        elif int(rent_time) > 7:
            if int(kind_car) == 1:
                fee = rent_time * 25
            elif int(kind_car) == 2:
                fee = rent_time * 40
            elif int(kind_car) == 3:
                fee = rent_time * 90
            else:
                raise ValueError("rent_car error")
            return fee
        else:
            raise ValueError("rent_time error")



    def add_carrent(self,cName,cartype,fee,days):
        """ for mainwindow"""
        a = len(self.df_win)
        self.df_win.loc[a+1]=[cName,cartype,fee,days]


    def add_carrent_ter(self,cartype, fee, days, isvip):
        """ for mainterminal"""
        a = len(self.df)
        self.df.loc[a + 1] = [self.cid, cartype, fee, days, isvip]



class VIP(Customer):
    """Customer definitions, inherited from the customer class, manage rental information """
    def __init__(self):
        super().__init__()
        self.isVIP=0

    def discount(self,kind_car,rent_time):
        fee = 0
        if rent_time > 0:
            if int(kind_car) == 1:
                fee = rent_time * 20
            elif int(kind_car) == 2:
                fee = rent_time * 35
            elif int(kind_car) == 3:
                fee = rent_time * 80
            else:
                raise ValueError("rent_car error")
        else:
            raise ValueError("rent_time error")
        return fee



