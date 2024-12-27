#hotel_admin.py

import creator as cr
import data as d
hotel_admin_list = []

class hotel_admin:
    def cus_issues(self, hot_n):
        while 1:
            print("1. View Customer Issues\n2. Exit")
            ci = int(input("I Want To : "))
            if(ci == 1):
                issue_found = False
                for i in cr.customer_issues:
                    if(i.get_hot() == hot_n):
                        issue_found = True
                        print(f"Food Item : {i.get_item()}, Issue : {i.get_rev()}")
                        break
                if not issue_found:
                    print("No Issues Sir..Happy Customers")
            elif(ci == 2):
                print(f"Exited From {hot_n}'s Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")

    def hot_adm_log(self):
        del_u = input("Enter Username : ")
        del_found = False
        for i in hotel_admin_list:
            if(del_u == i.get_user_name()):
                del_found = True
                del_p = input("Enter Password : ")
                if(del_p == i.get_pass()):
                    hot_n = i.get_hot()
                    print(f"Welcome To {hot_n}'s Page")
                    self.cus_issues(hot_n)
                else:
                    print("Oops! Invalid Password")
        if not del_found:
            print("<<<Register First>>>")

    def hot_adm_reg(self):
        hot_data = d.data()
        hot_data.set_hot(input("Enter Hotelname : "))
        user_name = input("Enter Username : ")
        for i in hotel_admin_list:
            if(i.get_user_name() == user_name):
                print("Username Already Exists")
                return
        hot_data.set_user_name(user_name)
        hot_data.set_pass(input("Enter Password : "))
        hotel_admin_list.append(hot_data)
        print("<<<Registration Successfull>>>")

    def hotel_admin_page(self):
        print("Welcome To Hotel Admin's Page")
        while 1:
            print("1. Register\n2. Login\n3. Exit")
            cu = int(input("Please Proceed : "))
            if(cu == 1):
                self.hot_adm_reg()
            elif(cu == 2):
                self.hot_adm_log()
            elif(cu == 3):
                print("Exited From Hotel Admin's Page")
                print("-"*20)
                break
            else:
                print("Invalid Option")