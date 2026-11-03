from datetime import datetime


class BankAccount:

    def __init__(self, account_holder, account_number,
                 balance, account_type, pin):

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.pin = pin

        self.transactions = []

    def display_details(self):

        print("\n===== ACCOUNT DETAILS =====")

        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: Ksh {self.balance}")

        def record_transaction(self, transaction_type, amount):

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "account_number": self.account_number
        }

        self.transactions.append(transaction)

    def transaction_history(self):

        print("\n===== TRANSACTION HISTORY =====")

        if not self.transactions:
            print("No transactions available.")

        for transaction in self.transactions:

            print(f"Type: {transaction['type']}")
            print(f"Amount: Ksh {transaction['amount']}")
            print(f"Date: {transaction['date']}")
            print(f"Account: {transaction['account_number']}")
            print("-------------------------")

    def transfer(self, receiver, amount, pin):

        if pin != self.pin:
            raise PermissionError("Incorrect PIN!")

        if self.account_number == receiver.account_number:
            raise ValueError("Cannot transfer to the same account.")

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance!")

        self.balance -= amount
        receiver.balance += amount

        self.record_transaction(
            "Transfer Sent",
            amount
        )

        receiver.record_transaction(
            "Transfer Received",
            amount
        )

        print("Transfer successful!")

