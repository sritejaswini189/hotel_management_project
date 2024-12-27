#home.py

import creator as cr
import hotel_admin as ha
import delivery_people as dp
import customer as cu

class zomato:
    def zom_log(self):
        while 1:
            print("Welcome To Zomata's Page\n1. Creator Login\n2. Hotel Admin's Login\n3. Delivery People's Login\n4. Customer's Login\n5. Exit")
            zom = int(input("I want to login as : "))
            if(zom == 1):
                cr.creator().creator_page()
            elif(zom == 2):
                ha.hotel_admin().hotel_admin_page()
            elif(zom == 3):
                dp.delivery_people().delivery_page()
            elif(zom == 4):
                cu.customer().customer_page()
            elif(zom == 5):
                print("Exit From Zomato's Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")

z = zomato()
z.zom_log()