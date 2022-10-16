def withdraw(t):
    w = int(input("Insert amount to withdraw: "))
    t -= w
    print(f"Withdrawal amount: {w} \nNew Total: {t}")
    return t


def deposit(t):
    d = int(input("Insert amount to deposit: "))
    t += d
    print(f"Deposited amount: {d} \nNew total: {t}")
    return t


total = int(input("Insert your account balance: "))
total = deposit(total)
total = withdraw(total)
def main