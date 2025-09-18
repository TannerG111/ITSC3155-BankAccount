from bankaccount import BankAccount
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

acc1 = BankAccount("Alice", 1020, 100, 123, 456)
acc2 = BankAccount("Bob", 5000, 10, 234, 567)

acc1.deposit(200)
acc1.withdraw(900)
acc1.print_customer_information()

acc2.deposit(100)
acc2.withdraw(501)
acc2.print_customer_information()

acc3 = SavingsAccount("Jim", 500, 390, 0.02, 454256, 4112)
acc4 = SavingsAccount("Sabrina", 1000, 205, 0.02, 45426, 5413)

acc3.deposit(200)
acc3.add_interest()
acc3.withdraw(900)
acc3.withdraw(200)
acc3.print_customer_information()

acc4.withdraw(501)
acc4.add_interest()
acc4.deposit(100)
acc4.print_customer_information()

acc5 = CheckingAccount("Tyler", 1200, 220, 100, 456, 32416)
acc6 = CheckingAccount("Isaac", 9000, 260, 200, 456, 324521)

acc5.deposit(200)
acc5.withdraw(900)
acc5.print_customer_information()

acc6.withdraw(199)
acc6.deposit(100)
acc6.print_customer_information()