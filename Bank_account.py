class BankAccount:
  def __init__(self, int_rate = 0.001, balance = 0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f'your current balance: {self.balance}')
    return self

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance -= amount
    else: print('insuffecient funds')
    return self
  def display_account_info(self):
    # your code here
    print(f'your current balance: {self.balance} and the interest rate is {self.int_rate}')
    return self
  def yield_interest(self):
    self.balance += (self.balance * self.int_rate)
    print(f'your current balance: {self.balance}')
    return self


acount_one = BankAccount(0.002, 100000)
acount_two = BankAccount(0.005, 1000000)

acount_one.deposit(100).deposit(1000).deposit(5000).withdraw(1000).display_account_info()
acount_two.deposit(10000).deposit(19922).withdraw(100).withdraw(1000).withdraw(190).withdraw(100).yield_interest().display_account_info()
