class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance        # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance
    
# Create a BankAccount object
account = BankAccount("123456", 1000)

# Access balance using method
print("Balance:", account.get_balance())

# Access the account_number public attribute
print("Account number:", account.account_number)

# Trying to access private attribute directly (will raise an error)
# print("Balance:", account.__balance)