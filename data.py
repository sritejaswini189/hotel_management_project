#data.py

class data:
    def __init__(self):
        self.__user_name = None
        self.__pass = None
        self.__email = None
        self.__mbl_num = None
        self.__name = None
        self.__add = None
        self.__hotel_name = None
        self.__item = None
        self.__rev = None

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
    
    def set_mbl(self, mbl):
        self.__mbl_num = mbl

    def get_mbl(self):
        return self.__mbl_num
    
    def set_pass(self, password):
        self.__pass = password

    def get_pass(self):
        return self.__pass
    
    def set_add(self, address):
        self.__add = address

    def get_add(self):
        return self.__add
    
    def set_hot(self, hot_name):
        self.__hotel_name = hot_name

    def get_hot(self):
        return self.__hotel_name
    
    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item
    
    def set_rev(self, review):
        self.__rev = review

    def get_rev(self):
        return self.__rev