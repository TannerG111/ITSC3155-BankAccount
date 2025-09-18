from bankaccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount}: Not enough money in balance\n")
        elif amount > self.transfer_limit:
            print(f"Cannot withdraw ${amount}: Amount specified '${amount}' is above transfer limit")
        else:
            super().withdraw(amount)

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Type: Checking Account")
        print(f"Transfer Limit: {self.transfer_limit:.2f}\n")