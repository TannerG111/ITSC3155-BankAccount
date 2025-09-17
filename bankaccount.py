class BankAccount:
    title = "Bank Incorporated"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount
        print(f"${amount} deposited. New balance: ${self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount}: Not enough money in balance")
        else:
            self.current_balance -= amount
            print(f"{self.customer_name} withdrew ${amount}. New balance: ${self.current_balance}")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.title}")
        print(f"Customer: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}\n ")

acc1 = BankAccount("Alice", 1000, 200)
acc2 = BankAccount("Bob", 500, 100)

acc1.deposit(200)
acc1.withdraw(900)
acc1.print_customer_information()

acc2.deposit(100)
acc2.withdraw(501)
acc2.print_customer_information()