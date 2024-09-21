class AccountRepository:
    def __init__(self, accounts):
        self.accounts = accounts

    def create_account(self, account_number, account_holder, initial_balance):
        # create a new bank account
        self.accounts.append({"account_number": account_number, "account_holder": account_holder, "balance": initial_balance})

    def delete_account(self, account_number):
        # delete a bank account
        self.accounts = [a for a in self.accounts if a["account_number"] != account_number]

class TransactionRepository:
    def __init__(self, transactions):
        self.transactions = transactions

    def add_transaction(self, transaction):
        # add a new transaction
        self.transactions.append(transaction)

class AccountService:
    def __init__(self, account_repository, transaction_repository):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def deposit(self, account_number, amount):
        # deposit money into a bank account
        for account in self.account_repository.accounts:
            if account["account_number"] == account_number:
                account["balance"] += amount
                self.transaction_repository.add_transaction({"type": "deposit", "account_number": account_number, "amount": amount})
                break

    def withdraw(self, account_number, amount):
        # withdraw money from a bank account
        for account in self.account_repository.accounts:
            if account["account_number"] == account_number:
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    self.transaction_repository.add_transaction({"type": "withdrawal", "account_number": account_number, "amount": amount})
                else:
                    print("Insufficient balance")
                break

class StatementGenerator:
    def __init__(self, transaction_repository):
        self.transaction_repository = transaction_repository

    def generate_statement(self, account_number):
        # generate a statement for a bank account
        statement = "Statement for account {}\n".format(account_number)
        for transaction in self.transaction_repository.transactions:
            if transaction["account_number"] == account_number:
                statement += "{}: {} {}\n".format(transaction["type"], transaction["amount"], "credited" if transaction["type"] == "deposit" else "debited")
        return statement