import unittest
import car_rental


class MyTestCase(unittest.TestCase):

    def test_fee(self):
        """ The cost of testing ordinary users """
        self.assertEqual(car_rental.Customer.fee('', 1, 5), 150)
        self.assertEqual(car_rental.Customer.fee('', 2, 5), 250)
        self.assertEqual(car_rental.Customer.fee('', 3, 5), 500)
        self.assertEqual(car_rental.Customer.fee('', 1, 8), 200)
        self.assertEqual(car_rental.Customer.fee('', 2, 8), 320)
        self.assertEqual(car_rental.Customer.fee('', 3, 8), 720)
        with self.assertRaises(ValueError):
             car_rental.Customer.fee('', 1, -19)
        with self.assertRaises(ValueError):
            car_rental.Customer.fee('', 4, 5)

    def test_discount(self):
        """ The cost of testing VIP users """
        self.assertEqual(car_rental.VIP.discount('', 1, 5), 100)
        self.assertEqual(car_rental.VIP.discount('', 2, 5), 175)
        self.assertEqual(car_rental.VIP.discount('', 3, 5), 400)
        self.assertEqual(car_rental.VIP.discount('', 1, 8), 160)
        self.assertEqual(car_rental.VIP.discount('', 2, 8), 280)
        self.assertEqual(car_rental.VIP.discount('', 3, 8), 640)
        with self.assertRaises(ValueError):
            car_rental.VIP.discount('', 4, 5)
        with self.assertRaises(ValueError):
            car_rental.VIP.discount('', 1, -1)

    """ The typos for rental and return are discussed separately in the main function, 
    so the value of the function entering the class must be correct and only changes the number of vehicles, 
    so there is no unit test for these two values here """
if __name__ == '__main__':
     unittest.main()

