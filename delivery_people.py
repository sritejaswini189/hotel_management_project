#delivery_people.py

import creator as cr
import data as d
delivery_people_list = []
customer_orders = []

class delivery_people:
    def del_log(self):
        del_u = input("Enter Username : ")
        del_found = False
        for i in delivery_people_list:
            if(del_u == i.get_user_name()):
                del_found = True
                del_p = input("Enter Password : ")
                if(del_p == i.get_pass()):
                    del_n = i.get_name()
                    print(f"Hello! {del_n}")
                    while 1:
                        if not customer_orders:
                            print("No Orders")
                            break
                        else:
                            for cus in customer_orders:
                                print(f"Name - {cus[0]}, Address - {cus[1]}, Item - {cus[2]}")
                                while 1:
                                    del_ok = input("I Delivered To (Customer Name) : ")
                                    name_found = False
                                    for j in customer_orders:
                                        if(del_ok == j[0]):
                                            name_found = True
                                            for i in cr.delivery_people_status:
                                                i[0] = del_n
                                                i[3] = 'Delivered'
                                            print(f"Deliver Success")
                                            customer_orders.remove(j)
                                            return
                                    if not name_found:
                                        print("Invalid Name To Deliver")
                else:
                    print("Invalid Password")
        if not del_found:
            print("Register First")

    def del_reg(self):
        del_data = d.data()
        del_data.set_user_name(input("Enter Username : "))
        del_data.set_pass(input("Enter Password : "))
        del_data.set_name(input("Enter Name : "))
        delivery_people_list.append(del_data)
        print("<<<Registration Successfull>>>")

    def delivery_page(self):
        print("Welcome To Delivery People's Page")
        while 1:
            print("1. Register\n2. Login\n3. Exit")
            cu = int(input("Enter : "))
            if(cu == 1):
                self.del_reg()
            elif(cu == 2):
                self.del_log()
            elif(cu == 3):
                print("Exited From Delivery People's Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")