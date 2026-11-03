from bank import Bank


bank = Bank()

bank.load_accounts()


def main():

    while True:

        print("\n====== SIMPLE BANKING SYSTEM ======")

        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Transaction History")
        print("8. Display All Accounts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                name = input("Enter account holder name: ")

                account_number = input("Enter account number: ")

                balance = float(input("Enter initial deposit: "))

                account_type = input("Enter account type: ")

                pin = input("Create a 4-digit PIN: ")

                if len(pin) != 4 or not pin.isdigit():
                    raise ValueError("PIN must contain 4 digits.")

                bank.create_account(
                    name,
                    account_number,
                    balance,
                    account_type,
                    pin
                )

            elif choice == "2":

                number = input("Enter account number: ")

                account = bank.find_account(number)

                amount = float(input("Enter deposit amount: "))

                account.deposit(amount)

            elif choice == "3":

                number = input("Enter account number: ")

                account = bank.find_account(number)

                pin = input("Enter your PIN: ")

                amount = float(input("Enter withdrawal amount: "))

                account.withdraw(amount, pin)

            elif choice == "4":

                number = input("Enter account number: ")

                account = bank.find_account(number)

                account.check_balance()

            elif choice == "5":

                sender_number = input("Enter sender account: ")

                receiver_number = input("Enter receiver account: ")

                sender = bank.find_account(sender_number)

                receiver = bank.find_account(receiver_number)

                pin = input("Enter your PIN: ")

                amount = float(input("Enter transfer amount: "))

                sender.transfer(receiver, amount, pin)

            elif choice == "6":

                number = input("Enter account number: ")

                account = bank.find_account(number)

                account.display_details()

            elif choice == "7":

                number = input("Enter account number: ")

                account = bank.find_account(number)

                account.transaction_history()

            elif choice == "8":

                bank.display_all_accounts()

            elif choice == "9":

                bank.save_accounts()

                bank.save_transactions()

                print("Thank you for using our banking system!")

                break

            else:

                print("Invalid choice. Please try again.")

        except (ValueError, PermissionError) as error:

            print(f"Error: {error}")

        except Exception as error:

            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":

    main()