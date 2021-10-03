# Bank
# Made by somePythonProgrammer as a WhiteHat project.
# This is an example on how to use classes.

class User:
    """
    This class is used to create a user.
    """

    def __init__(self):
        self.name = input("Please enter your name: ")
        while True:
            self.pin = input("Please enter your pin: ")
            pin_temp = input("Please confirm your pin: ")
            if self.pin == pin_temp:
                break
            else:
                print("Pins do not match. Please try again.")

        self.balance = 1000
        self._tries_login = 0
        self.account_disabled = False

    def get_name(self):
        if self.account_disabled:
            return "Account disabled"
        else:
            return self.name

    def get_balance(self):
        if self.account_disabled:
            return "Account disabled"
        else:
            return self.balance

    def confirm_pin(self, pin):
        if self.account_disabled:
            return "Account disabled"
        else:
            if self.pin == pin:
                self._tries_login = 0
                return True
            else:
                self._tries_login += 1
                if self._tries_login == 3:
                    print("Too many tries. THE ACCOUNT HAS BEEN DISABLED!")
                    self.account_disabled = True
                else:
                    print("Incorrect pin. Please try again.")
                    return False
                return False


class Bank:
    def __init__(self, name):
        print("Welcome to {}!".format(name))
        self.name = name

    def deposit(self, user, amount):
        if self.ask_password(user):
            if not user.account_disabled:
                user.balance += amount
                return user.balance
            else:
                print("You can't deposit money, your account is disabled.")

    def withdraw(self, user, amount):
        if self.ask_password(user):
            if not user.account_disabled:
                user.balance -= amount
                return user.balance
            else:
                print("You can't withdraw money, your account is disabled.")

    def ask_password(self, user):
        password = input("Enter your password: ")
        if user.confirm_pin(password):
            return True
        else:
            return False


if __name__ == "__main__":
    bank = Bank("Bank of Python")
    users = [User()]
    current_user = 0
    while True:
        choice = str(input(
            "What do you want to do (withdraw/deposit/balance/newuser/switchuser/deleteuser/exit): "))
        if choice == "withdraw":
            amount = int(input("Enter amount to withdraw: "))
            print("Your new balance is {}".format(
                bank.withdraw(users[current_user], amount)))
        elif choice == "deposit":
            amount = int(input("Enter amount to deposit: "))
            print("Your new balance is {}".format(
                bank.deposit(users[current_user], amount)))
        elif choice == "balance":
            print("Your balance is {}".format(users[current_user].get_balance()))
        elif choice == "newuser":
            user = User()
            users.append(user)
            current_user = len(users) - 1
        elif choice == "switchuser":
            temp =  [data.name for data in users].index(input("Enter user name: "))
            temp_ =  [data.pin for data in users].index(input("Enter password: "))
            current_user = temp if temp != current_user and temp == temp_ else current_user
            print(f'Current user: {users[current_user].get_name()}')
        elif choice == "deleteuser":
            if users[current_user].confirm_pin(input("Enter your pin: ")):
                del users[current_user]
                print('Successfully deleted.')
                try:
                    temp = users[current_user]
                except IndexError:
                    current_user = 0
                    print(f'Current user: {users[current_user].get_name()}')
        elif choice == "exit":
            print("Thank you for using {}!".format(bank.name))
            break
        else:
            print("Invalid choice. Please try again.")

# EOF
