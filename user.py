class User:
  def __init__(self, name, balance) -> None:
    self.name = name
    self.balance = balance
  def show_balance(self):
    print(f'your blance: {self.balance}')
  def deposit(self, amount):
    self.balance += amount
    print(f'')

  def withdrawal(self, amount):
    self.balance -= amount
    print(f'withdrawal amount: {str(amount)}')

  def transfer_money(self, amount, other_user):
    self.balance -= amount
    other_user.balance += amount
    print(f'{str(amount)}$ has been transfered to{other_user.name}')

# I was explaining to laith have fun if you are reading this and give me extra credits :D
class Other_user(User):
  def __init__(self, name, balance) -> None:
    super().__init__(name, balance)

moh = Other_user('saleem', 9000)
moh.show_balance()
class Dog:
  def __init__(self,name, breed, num_legs) -> None:
    self.name = name
    self.breed = breed
    self.num_legs = num_legs
  def bite(self):
    print('woof woof')

  def bark(self):
    print('AHHHHHHHHHH  ERHAMNIIIIIII')

lion = Dog('laith', 'nabulsi', 3)
lion.bark()
saeed = User('saeed', 1000000000)
saeed.deposit(110)
saeed.deposit(20000)
saeed.withdrawal(10000)
print(saeed.balance)
laith = User('laith', 70)
laith.deposit(200)
saeed.transfer_money(100000, laith)
laith.withdrawal(1000)
laith.withdrawal(20)
laith.withdrawal(1111)

print(laith.show_balance())

ahmad = User('ahmad', 1000)
laith.transfer_money(100, laith)


