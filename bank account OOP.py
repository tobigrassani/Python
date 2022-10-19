class Person:
    def __init__(self, name, gender, id):
        self.name = name
        self.gender = gender
        self.id = id

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Account:
    def __init__(self):
        self.balance = 0
        print(">>> Hello!! Welcome to ATM <<<")

    def deposit(self):
        amount = int(input("\nEnter the amount to be deposited: "))
        self.balance += amount
        print(f"\nAmount deposited: ${amount} Usd")

    def withdraw(self):
        amount = -1
        while amount <= 0:
            amount = int(input("\nEnter the amount to be withdrawn: "))
            if amount == 0:
                print("Minimum to be withdrawn: $1 Usd")
                continue
            if self.balance < amount:
                print("Insufficient balance")
            else:
                print(f"\nAmount withdrawn: ${amount} Usd")
                self.balance -= amount

    def display(self):
        print(f"\nYour balance is ${self.balance} Usd")


def main():
    opt = True
    while opt is True:
        print("""\n
        Menu Options:
        1. Create Account
        2. Deposit
        3. Withdraw
        0. Exit""")
        opt = int(input("\nInsert option: "))
        if opt == 1:
            new_account = Account()
            print("\nAccount Created Successfully")
            opt = True
        if opt == 2:
            new_account.deposit()
            opt = True
        if opt == 3:
            new_account.withdraw()
            opt = True
        if opt == 0:
            print("\nThanks for using our machine.")
            break


main()




