class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # deposit money into the account
        self.balance += amount

    def withdraw(self, amount):
        # withdraw money from the account
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

class Send_Statement:
    def send_statement(self):
        # send a statement to the account holder
        print(f"Sending statement to account holder for account {self.account_number}...")

class Calculate_Interest:
    def calculate_interest(self):
        # calculate interest on the account balance
        return self.balance * 0.05

class Update_Account_Status:
    def update_account_status(self):
        # update the account status in the database
        print(f"Updating account status for account {self.account_number}...")