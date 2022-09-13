from Bank_account import BankAccount

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {}


  def deposit(self, amount, account_name):
    self.accounts[account_name].deposit(amount)
    print(self.accounts[account_name].balance)
    return self

  def withdraw(self, amount, account_name):
    self.accounts[account_name].withdraw(amount)
    return self

  def display_account_info(self, account_name):
    self.accounts[account_name].display_account_info()
    return self

  def yield_interest(self, account_name):
    self.accounts[account_name].yield_interest()
    return self

  def create_new_account(self, account_name, rate=0.02, balance=0):
    self.accounts[account_name] = BankAccount(rate, balance)
    print('account created successfully')



ahmad = User('ahmad', 'ahmad@email.com')
ahmad.create_new_account('arab-bank', 0.02, 50000)
ahmad.create_new_account('anotherone', 0.2, 5000)
ahmad.create_new_account('BOA', 0.2, 5000000)
ahmad.deposit(100000, 'arab-bank')
ahmad.withdraw(1000, 'arab-bank')
ahmad.withdraw(1000, 'anotherone')
ahmad.display_account_info('anotherone')
ahmad.display_account_info('arab-bank')
ahmad.yield_interest('BOA')