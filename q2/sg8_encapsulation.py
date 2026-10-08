class BankAccount: #create class called BankAccount
    def __init__(self, account_number, balance): #sets properties of class
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number): #setter method for account number
        self.__account_number = account_number

    def set_balance(self, balance): #setter method for balance 
        if balance >= 0: #checks if balance is negative
            self.__balance = balance
        else: 
            print("The balance must not be a negative number.") #warning for negative number

    @property #@property decorator
    def get_account_number(self):
        return self.__account_number

    @property #@property decorator
    def get_balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000) #Object for BankAccount class

a1.set_account_number(12345) #Sets the properties according to object
a1.set_balance(1000)

print("Account 1")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: ₱{a1.get_balance:,.2f}")

a1.set_balance(-100)
print(f"Balance: ₱{a1.get_balance:,.2f}")


