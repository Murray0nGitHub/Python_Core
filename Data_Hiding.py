#You are given a BankAccount class and need to add a deposit() method to it, which adds the given amount to the private balance property.

#The code should declare a BankAccount object with an initial balance of 0, take a number from user input, add it to the balance using the deposit() method, and output the object.

#Complete the required deposit() method so the code works as expected and produces the required output.
#Remember, the methods in a class need to have self as their first parameter, which is used to access the properties.


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
        return "Account Balance: {}".format(self._balance)

    def deposit(self, amount):
        self._balance += amount


acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)