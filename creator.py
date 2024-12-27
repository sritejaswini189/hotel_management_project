#creator.py

import hotel_admin as ha
hotel_details = [['starbellies', [['Idly', 60], ['Parota', 90], ['Dosa', 100]]], 
                 ['Ambika', [['Chicken Biryani', 250], ['Veg Friedrice', 200]]],
                 ['KFC', [['Chicken Rolls', 200], ['Chicken Bucket', 700]]]]
delivery_people_status = []
customer_issues = []

class creator:
    def creator_page(self):
        cre_id = 'teju'
        cre_pass = '111'
        a = input("Enter Creator Id : ")
        b = input("Enter Creator Password : ")
        if(a == cre_id and b == cre_pass):
            print("<<<Welcome My Creator>>>")
            while 1:
                print("1. Hotel Names\n2. Customer Issues\n3. Delivery Status\n4. Exit")
                cr = int(input("I Want To View : "))
                if(cr == 1):
                    for i in hotel_details:
                        print(f"-->{i[0]}")
                elif(cr == 2):
                    issues_found = False
                    for i in customer_issues:
                        issues_found = True
                        print(f"-->Hotel - {i.get_hot()}, Item - {i.get_item()}, Issue - {i.get_rev()}")
                    if not issues_found:
                        print("No Issues")
                elif(cr == 3):
                    status_found = False
                    for i in delivery_people_status:
                        status_found = True
                        print(f"-->Deliver By - {i[0]}, Deliver To - {i[1]}, Item - {i[2]}, Status - {i[3]}")
                    if not status_found:
                        print("No Deliveries Still Now")
                elif(cr == 4):
                    print("Exited From Creator Page")
                    print("-"*20)
                    break
                else:
                    print("Invalid Option")
        else:
            print("Oops! Invalid Creditnals My Creator")

