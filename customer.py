#customer.py

import creator as cr
import delivery_people as dp
import data as d

customer_list = []

class customer:
    def ord_food(self, cus_name, cus_address):
        print(F"{cus_name}! Are You Hungry..Please Order Your food")
        for i in cr.hotel_details:
            hotel = i[0]
            food_items = i[1]
            items = []
            for j in food_items:
                items.append(f"{j[0]} - {j[1]}")
            print(f"Hotel - {hotel}",end = "-->")
            print("Items : ", ", ".join(items))
        while 1:
            print("1. Food Order\n2. Food Review\n3. Exit")
            ord_item = int(input("I Want To Give : "))
            if(ord_item == 1):
                item_found = False
                while 1:
                    user_item = input("Select item to order : ")
                    for i in cr.hotel_details:
                        food_items = i[1]
                        for j in food_items:
                            if(user_item == j[0]):
                                item_found = True
                                item_payment = int(input("Payment : "))
                                if(item_payment == j[1]):
                                    cus_ord_det = [cus_name, cus_address, user_item]
                                    dp.customer_orders.append(cus_ord_det)
                                    cus_status = [None, cus_name, user_item, 'Not Delivered']
                                    cr.delivery_people_status.append(cus_status)
                                    print(f"{cus_name} Your Order Confirmed")
                                    return
                                else:
                                    print("Insufficient Payment")
                        if not item_found:
                            print("No Item")
                            break
            elif(ord_item == 2):
                ord_data = d.data()
                ord_data.set_hot(input("Enter Hotel Name : "))
                ord_data.set_item(input("Enter Item Name : "))
                ord_data.set_rev(input("Please Write Your Review : "))
                cr.customer_issues.append(ord_data)
                print(f"{cus_name}! We Received Your Review")
            elif(ord_item== 3):
                print(f"--{cus_name}! Thankyou Visit Again--")
                break
            else:
                print("Oops! Invalid Option")

    def cus_log(self):
        cus_u = input("Enter Username : ")
        cus_found = False
        for i in customer_list:
            if(cus_u == i.get_user_name()):
                cus_found = True
                cus_p = input("Enter Password : ")
                if(cus_p == i.get_pass()):
                    cus_name = i.get_name()
                    cus_address = i.get_add()
                    print(f"--Welcome To {cus_name}'s Page--")
                    self.ord_food(cus_name, cus_address)
                else:
                    print("Invalid Password")
        if not cus_found:
            print("Register First")

    def cus_reg(self):
        cus_data = d.data()
        user_name = input("Enter Username : ")
        for i in customer_list:
            if(i.get_user_name() == user_name):
                print("Username Already Exists")
                return
        cus_data.set_user_name(user_name)
        cus_data.set_pass(input("Enter Password : "))
        cus_data.set_name(input("Enter Name : "))
        cus_data.set_mbl(int(input("Enter Mobile Number : ")))
        cus_data.set_add(input("Enter Address : "))
        customer_list.append(cus_data)
        print("<<<Registration Successfull>>>")
        
    def customer_page(self):
        print("Welcome To Customer's Page")
        while 1:
            print("1. Register\n2. Login\n3. Exit")
            cu = int(input("Enter : "))
            if(cu == 1):
                self.cus_reg()
            elif(cu == 2):
                self.cus_log()
            elif(cu == 3):
                print("Exited From Customer's Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")