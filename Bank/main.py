from bankaccount import BankAccount
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

acc1 = BankAccount("Alice", 1000, 200)
acc2 = BankAccount("Bob", 500, 100)

acc1.deposit(200)
acc1.withdraw(900)
acc1.print_customer_information()

acc2.deposit(100)
acc2.withdraw(501)
acc2.print_customer_information()
