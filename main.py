from bank import BankAccount



michael= BankAccount(2,500)
alvaro= BankAccount(4,8000)





michael.deposit(500).deposit(700).deposit(400).withdraw(200).display_account_info()

alvaro.deposit(100).deposit(200).withdraw(100).withdraw(2000).withdraw(200).withdraw(500).display_account_info()