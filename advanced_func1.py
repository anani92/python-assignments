import random

def randInt(min= 0  , max= 100  ):
    if min > max or min < 0 or max < min or max <0:
      return
    num = random.randrange(min, max)
    return round(num)



print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))

