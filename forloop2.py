def biggie_size(nums):
  for i in range(len(nums)):
    if nums[i] >= 0:
      nums[i] = 'big'
  return nums
print(biggie_size([-1, 3, 5, -5]))

def count_positives(list):
  length = len([num for num in list if num > 0])
  list[-1] = length
  return list
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(list):
  return sum(list)
print(sum_total([1,2,3,4]) )

def average(list):
  avg = sum(list) / len(list)
  return avg

def length(list):
  return len(list)

def minimum(list):
  if list:
    return min(list)
  return False

def maximum(list):
  max = 0
  for num in list:
    if num > max:
      max = num
  return max

def ultimate_analysis(list):
  analysis = {
    'sumTotal': sum(list),
    'average': (sum(list)/ len(list)),
    'minimum': min(list),
    'maximum': max(list),
    'length': len(list)
    }
  return analysis

print(ultimate_analysis([37,2,1,-9]))


def reverse_list(list):
  reverse = []
  for i in range(len(list), 0):
    reverse.append(list[i])
  return reverse

for num in range(0,100):
  print(num)




