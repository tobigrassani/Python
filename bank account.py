def withdraw(t):
    print("Balance available: ", t)
    w = int(input("Insert amount to withdraw: "))
    t -= w
    print(f"Withdrawal amount: {w} \nNew Total: {t}")
    return t


def deposit(t):
    print("Balance available: ")
    d = int(input("Insert amount to deposit: "))
    t += d
    print(f"Deposited amount: {d} \nNew total: {t}")
    return t


option = True
total = 0
while option > 0 & option < 4:
    print("""
    Hello! Welcome to ATM
    Choose an option from below:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    """)
    option = int(input("Insert option: "))
    if option == 1:
        print(f"Your available balance is ${total} dollars")
    if option == 2:
        total = deposit(total)
    if option == 3:
        total = withdraw(total)
    if option == 4:
        break
else:
    print("Please")


