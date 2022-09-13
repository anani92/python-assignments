class User:
  def __init__(self, name, email, age, balance):
    self.name=name
    self.email=email
    self.age=age
    self.balance=balance
  def withdraw(self , amount ):
    if amount < self.balance:
      self.balance -= amount
    else:
      print('insuffecient funds')
    return self
  def display_user_balance(self):
    print(f"{self.name} Balance is :{self.balance}")
    return self
  def deposit(self,amount):
    self.balance += amount
    return self
  def transfer_money(self, other_user, amount):
    if amount < self.balance:
      self.balance -= amount
      other_user.balance += amount
      print(f'{amount}$ has been transfered to {other_user.name}')
    else:
      print('insuffecient funds')
    return self

saeed = User('saeed', 'saeed@email.com', 25, 10000)
ahmad = User('ahmad', 'ahmad@email.com', 23, 100000)
ali = User('ali', 'ali@email.com', 29, 1000000)

saeed.deposit(100).deposit(2999).deposit(9000).withdraw(20000).display_user_balance()

ahmad.deposit(2999).deposit(9000).withdraw(20000).display_user_balance()



ali.deposit(100).withdraw(20000).withdraw(20000).withdraw(20000).transfer_money(ahmad, 1000).display_user_balance()

