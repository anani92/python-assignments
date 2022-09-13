def countdown(num):
  return [i for i in range(num, 0)]

def printandReturn(list):
  print(list[0])
  return list[-1]

def first_plus_length(list):
  return list[0] + len(list)

def values_greater_than_second(list):
  greater_values = [num for num in list if num > list[1]]
  print(len(greater_values))
  if(len(greater_values > 2)):
    return greater_values
  else:
    return False

def length_and_value(length, value):
  values = []
  for i in range(length):
    values.append(value)
  return values

print(length_and_value(5,4))