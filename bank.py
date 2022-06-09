def decorator(func):
    def wrapper(*args, **kwargs):
        print("Action completed")
        func(*args, **kwargs)
    return wrapper


import time
import acc

class Banckaccount(object):
    name_of_bank = "CSS INTERNATIONAL BANK"
    

    def __init__(self, name, passw, balance):
        self.name = name
        self.passw = passw
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited..")
        return self.balance

        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn..")
            return self.balance
        else:
            print("Insufficient balance")
        
    def __str__(self):
        return f"User: {self.name} --------> Balance: {self.balance}"




def create_account():
    file = open("acc.py", "a")
    name = input("Please enter your name: ")
    password = input("Please set your password: ")
    file.write("\n{} = ['{}', {}]".format(name, password, 0))



def main():
    file = open("acc.py", "a")
    name = input("Enter your name: ")
    try:
        user = eval(f"acc.{name}")
        passw = user[0]
        print("Please wait.....")
        time.sleep(2)
        password = input("Enter your password: ")
        if passw != password:
            print(f"incorrect password")
            exit()
        
        balance = user[1]
        main_user = Banckaccount(name, passw, balance)
        action = input("Deposit[d]-------Withdraw[w]")
        if action.lower() == "d":
            amount = input("Enter amount: \n")
            print("please wait")
            time.sleep(2)
            balance = main_user.deposit(int(amount))
            file.write("\n{} = ['{}', {}]".format(name, passw, balance))


        elif action.lower() == "w":
            amount = input("Enter amount: \n")
            print("please wait")
            time.sleep(2)
            balance = main_user.withdraw(int(amount))
            file.write("\n{} = ['{}', {}]".format(name, passw, balance))

        else:
            print("Incorrect choice....")
            exit()



    except AttributeError:
        print("Account does not exit....")

if __name__ == "__main__":

    about = input("Do you already have an account (y/n): ")
    if about == "y":
        main()
    else:
        create_account()

    