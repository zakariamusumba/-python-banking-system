# -python-banking-system

# Banking Application

## 1. Project Overview

The **Banking Application** is a Python-based banking management system designed to manage customer accounts, perform financial transactions, and store banking information securely using JSON files.

The application allows multiple customers to manage their accounts, check balances, deposit money, withdraw money, and view transaction records.

## 2. Project Structure

The project is organized into the following files:

```text
Banking_Application/
│
├── main.py
├── bank_account.py
├── bank.py
├── transaction.py
├── accounts.json
└── transactions.json
```

## 3. File Descriptions

### 1. main.py
- Acts as the main entry point of the application.
- Runs the banking application.
- Displays the banking menu.
- Accepts user input.
- Connects the different Python modules.

### 2. bank_account.py
- Defines the BankAccount class.
- Handles customer account information.
- Manages account balances.
- Supports deposits and withdrawals.
- Validates account operations and PINs.

### 3. bank.py
- Defines the Bank class.
- Manages multiple customer accounts.
- Handles account creation and account searches.
- Coordinates banking operations.

### 4. transaction.py
- Handles financial transactions.
- Records deposits and withdrawals.
- Maintains transaction information.
- Supports transaction history tracking.

### 5. accounts.json
- Stores customer account information.
- Stores account holder names and account numbers.
- Stores account balances and account types.
- Stores PIN information and account transaction records.

### 6. transactions.json
- Stores transaction records.
- Maintains records of financial activities.
- Helps preserve transaction information between application sessions.

## 4. Main Features

- **Account Management:** Create and manage multiple customer accounts.
- **Deposits:** Allow customers to deposit money.
- **Withdrawals:** Allow customers to withdraw money.
- **Balance Checking:** Display the current account balance.
- **PIN Verification:** Verify customer PINs before authorized operations.
- **Transaction History:** Keep records of financial transactions.
- **Data Persistence:** Store account and transaction information using JSON files.
- **Input Validation:** Prevent invalid user input and incorrect transactions.
- **Exception Handling:** Handle errors during banking operations.

## 5. Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)
- Exception Handling
- File Handling
- Dictionaries and Lists
- Functions and Classes

## 6. Installation and Setup

### Requirements
- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.
- A terminal or command prompt.

### Steps

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Ensure all six files are in the correct project directory.
4. Open the terminal.
5. Run the application using:

```bash
python main.py
```

## 7. Python Concepts Applied

The project demonstrates the following Python programming concepts:

1. **Classes and Objects:** Used to represent bank accounts, banks, and transactions.
2. **Encapsulation:** Organizes account information and related operations.
3. **Inheritance:** Can be used to extend banking functionality where required.
4. **Functions:** Used to organize reusable operations.
5. **Dictionaries:** Used to manage customer and account information.
6. **File Handling:** Used to read and write banking data.
7. **JSON:** Used for persistent data storage.
8. **Exception Handling:** Uses error handling to manage unexpected situations.
9. **Conditional Statements:** Used to control banking operations.
10. **Loops:** Used to keep the application running until the user exits.

## 8. Validation and Error Handling

The application considers the following validation cases:

- Rejecting incorrect PINs.
- Preventing withdrawals exceeding the available balance.
- Rejecting negative or invalid transaction amounts.
- Checking whether an account exists.
- Preventing invalid customer information.
- Handling missing or invalid JSON data.
- Handling unexpected errors during transactions.

## 9. Limitations

- The application uses local JSON files instead of a database.
- It does not support real banking or mobile money integration.
- It does not provide online banking services.
- JSON storage is not suitable for large-scale banking systems.
- Additional security measures are required to protect sensitive customer information.

## 10. Future Improvements

Future versions could include:

- Integration with a database such as MySQL or PostgreSQL.
- Improved PIN encryption and password security.
- A graphical user interface.
- Online banking services.
- Mobile banking integration.
- Account-to-account transfers.
- Automated receipts and downloadable statements.
- Improved administrator functionality.

## 11. Conclusion

The Banking Application demonstrates how Python can be used to develop a basic banking management system. It combines Object-Oriented Programming, JSON file storage, validation, exception handling, and transaction management to provide a structured banking solution.

The project also provides a foundation for developing more advanced banking applications in the future.

---

**Project Name:** Banking Application  
**Programming Language:** Python  
**Storage:** JSON  
**Project Type:** Banking Management System  
**Version:** 1.0
