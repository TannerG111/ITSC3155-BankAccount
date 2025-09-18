from bankaccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.current_balance * self.interest_rate
        self.current_balance += interest_amount
        print(f"Interest of {interest_amount:.2f} added. New balance: {self.current_balance:.2f}")

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Type: Savings Account")
        print(f"Interest Rate: {self.interest_rate:.2f}\n")
