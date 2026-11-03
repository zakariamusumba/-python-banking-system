from bank_account import BankAccount


class Bank:

    def __init__(self):

        self.accounts = {}

    def create_account(self, name, account_number,
                       balance, account_type, pin):

        if account_number in self.accounts:
            raise ValueError("Account number already exists!")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        account = BankAccount(
            name,
            account_number,
            balance,
            account_type,
            pin
        )

        self.accounts[account_number] = account

        print("Account created successfully!")

        return account

    def find_account(self, account_number):

        if account_number not in self.accounts:
            raise ValueError("Account not found!")

        return self.accounts[account_number]

    def display_all_accounts(self):

        for account in self.accounts.values():

            account.display_details()

if account_number in self.accounts:
    raise ValueError("Account number already exists!")

import json

with open("accounts.json", "w") as file:
    json.dump(data, file, indent=4)

with open("accounts.json", "r") as file:
    data = json.load(file)