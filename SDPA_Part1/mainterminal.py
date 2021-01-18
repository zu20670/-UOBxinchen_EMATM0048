import car_rental as car

NewCars=car.Carsshop()
NewCustomer=car.Customer()
NewVIP=car.VIP()


def run():
    """The main running function """
    print("*" * 50)
    #Declare action options
    options=['0.rent','1.return','2.exit']
    #Information output
    print('WELCOME TO CAR RENTAL SYSTEM')
    for i in range(3):
        print('%s  ' %options[i], end='')
    try :
        choice=int(input('Please enter options:(enter the number)'))
        #Input judgment
        if choice== 0:
            print('%s' %options[choice])
            car_rent()
        elif  choice== 1:
            print('%s' % options[choice])
            car_return()
        elif choice==2:
            exit()
        else:
            print('Incorrect number option')
    except ValueError:
        print('The input is not a number')
    run()


def select_car():
    # Declare action options
    options = ['1.Hatchback', '2.Sedan', '3.SUV']
    # Information output
    print("Please choose the type of car")
    for i in range(3):
        print('%s  ' % options[i], end='')
    try:
        choice = int(input('Please enter options:(enter the number)'))
        # Input judgment
        if choice == 1:
            print('%s' % options[choice-1])
            return '1'
        elif choice == 2:
            print('%s' % options[choice-1])
            return '2'
        elif choice == 3:
            print('%s' % options[choice-1])
            return '3'
        else:
            print('Incorrect number option')
            ret = select_car()
            return ret
    except ValueError:
            print('The input is not a number')
            ret = select_car()
            return ret


def select_time():
    #Ask the user to input the time and determine the content of the input
    iVal = input('Please input the time(day) to borrow the car(enter the number)')
    if int(iVal) > 0:
        print('The time you select is %d days' %int(iVal))
        return int(iVal)
    else:
        print('The input time is incorrect')
        ret = select_time()
        return ret

def calulatefee(cartype,renttime,isvip):
    # Computational cost
    if isvip==0:
        fee=NewCustomer.fee(cartype,renttime)
    else:
        fee=NewVIP.discount(cartype,renttime)
    return fee

def isVIP():
    # Ask the user to input the vip imformation and determine the content of the input
    print("Are you a VIP?")
    options = ['1.YES', '0.NO']
    # Information output
    for i in range(2):
        print('%s  ' % options[i], end='')
    try:
        choice = int(input('Please enter options:(enter the number)'))
        # Input judgment
        if choice == 1:
             return 1
        elif choice == 0:
            return 0
        else:
            print('Incorrect number option')
            ret = isVIP()
            return ret
    except ValueError:
        print('The input is not a number')
        ret = isVIP()
        return ret


def car_rent():
    # Car_rent function
    print("-"* 50)
    print('''The garage inventory: 
    Hatchback: %d", 
    Sedan: %d, 
    SUV: %d''' %(NewCars.num_hatchback,NewCars.num_sedan,NewCars.num_suv))
    print("-"* 50)#The output of inventory
    car_type = select_car()
    # Output information of successfully borrowed car
    if NewCars.rent_car(car_type):
        renttime = select_time()
        isvip = isVIP()
        fee = calulatefee(car_type, renttime, isvip)
        NewCustomer.add_carrent_ter(car_type, fee, renttime, isvip)
        rentnum = NewCustomer.cid
        NewCustomer.cid += 1
        if car_type == '1':
            carname = 'Hatchback'
        elif car_type == '2':
            carname = 'Sedan'
        elif car_type == '3':
            carname = 'SUV'
        INFO = 'You have rented a {} car for {} days. You will be charged {} pounds, Your order number is: {}, Congratulations on your successful car rental！We hope that you enjoy our service.'.format(carname,
            renttime, fee, rentnum)
        print("-" * 50)
        print(INFO)
        print("-" * 50)
    else:
        print('Your choice of vehicles is already insufficient')
        car_rent()



def car_return():
    # Return_car function
    if NewCustomer.df.empty:
        print('No record of borrowing a car')
        return
    else:
        print("-" * 50)
        print(NewCustomer.df)
        print("-" * 50)
        iVal = input('Please enter your order number(enter the number)')
        infolist = NewCustomer.df[NewCustomer.df.ORDER_ID== int(iVal)]
        if infolist.empty:
            print('Incorrect order number')
        else:
            #Print a receipt
            a = infolist.index.tolist()
            carname = ''
            select_car = infolist.iat[0, 1]
            FEE = infolist.iat[0, 2]
            print(infolist)
            NewCustomer.df.drop(a[0], inplace=True)
            NewCars.return_car(select_car)
            if select_car == '1':
                carname = 'Hatchback'
            elif select_car == '2':
                carname = 'Sedan'
            elif select_car == '3':
                carname = 'SUV'
            Message_return = 'You have successfully returned a {} car, the total cost is {}.'.format(carname, FEE)
            print("-" * 50)
            print(Message_return)
            print("-" * 50)




