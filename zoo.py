class Animal:
  def __init__(self, name, health, happiness, age) -> None:
    self.name = name
    self.health = health
    self.happiness = happiness
    self.age = age
  def display_info(self):
    print(f'{self.name}is {self.age} old and happiness level {self.happiness} and health percentage {self.health} ')
  def feed(self):
    self.health += 10
    self.happiness += 10
    return self
  def happy_birthday(self):
    self.age += 1
    print(f'{self.name} birthday and he is  {self.age} years old')
    return self
  def play(self):
    self.happiness += 5
    print(f'{self.name} is happy')
    return self

class Lion(Animal):
  def __init__(self, name, health, happiness, age):
    super().__init__(name, health, happiness, age)
    self.food = 'meat'
    self.type = 'predators'

  def feed(self, food):
    if food == self.food:
      print('yum yum yum')
    else:
      print('Gross!!!')
    super().feed()
    return self

class Tiger(Animal):
  def __init__(self, name, health, happiness, age):
    super().__init__(name, health, happiness, age)
    self.type = 'predators'
    self.food = 'chicken'
  def feed(self, food):
    if self.food == food:
      print('yummy')
    super().feed(food)
    return self


class Zoo:
  def __init__(self, zoo_name):
    self.animals = []
    self.name = zoo_name
  def add_lion(self, name,  health, happiness, age):
    self.animals.append( Lion(name, health, happiness, age) )
    return self
  def add_tiger(self, name,  health, happiness, age):
    self.animals.append( Tiger(name, health, happiness, age) )
    return self
  def print_all_info(self):
    print("-"*30, self.name, "-"*30)
    for animal in self.animals:
        animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",100, 100, 10)
zoo1.add_lion("Simba",112, 90,10)
zoo1.add_tiger("Rajah", 30, 90, 29)
zoo1.add_tiger("Shere Khan",20, 20, 19)
zoo1.print_all_info()
nala = zoo1.animals[0]
nala.feed('meat').feed('checken').play().happy_birthday()
