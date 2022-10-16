def withdraw(t):
    print("---------- WITHDRAW ----------")
    print("Available balance: $", t)
    w = int(input("Insert amount to withdraw: "))
    if (t - w) > 0:
        t -= w
        print(f"Withdrawal amount: ${w} \nNew Total: ${t}")
    else:
        print("\nYou don't have enough balance.")
        print("Available balance: $", t)
    return t


def deposit(t):
    print("---------- DEPOSIT ----------")
    print("Available balance: $", t)
    d = int(input("Insert amount to deposit: $"))
    t += d
    print(f"Deposited amount: ${d} \nNew total: ${t}")
    return t


def exitmenu():
    print("""
    Choose an option from below:
    1. Back to Menu
    0. Exit""")
    x = int(input("Insert option: "))
    while x != 1:
        if x == 0:
            break
        x = int(input("Insert a valid option: "))
    return x


def login():
    user = input("Login \nUser: ")
    password = input("Password: ")
    access = user + password
    if (user + password) == access:
        print("Login successful")
        system()
    else:
        print("Login denied")


def system():
    total = 0
    option = True
    while option:
        print("---------- ATM MENU ----------")
        print("""
        Hello! Welcome to ATM
        Choose an option from below:1
        1. Check Balance
        2. Deposit
        3. Withdraw
        0. Exit
        """)
        option = int(input("Insert option: "))
        while option < 0 or option > 4:
            option = int(input("Insert a valid option: "))
        if option == 1:
            print(f"\nYour balance is ${total} dollars")
            option = exitmenu()
        elif option == 2:
            total = deposit(total)
            option = exitmenu()
        elif option == 3:
            total = withdraw(total)
            option = exitmenu()
        elif option == 0:
            break
        else:
            print("Choose a correct option please")


def main():
    login()


main()

