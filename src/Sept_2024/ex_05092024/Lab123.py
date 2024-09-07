class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number # private

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print("The account number is :" ,self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_method(self): # Private method --> __internal_method --> It can access private variable / public variable
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()



icici = Bank(9876543210, 100)
# icici.__init__() Cannot be accessed, as its private
icici.deposit(100)
icici.check_balance()
icici.show_me_account_number(False) # Not Allowed
icici.show_me_account_number(True) # True --> Authenticated


icici.deposit(100)
icici.check_balance()
# icici.__internal_method() - Error / Not allowed to access