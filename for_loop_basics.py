for i in range(0, 150):
  print(i)

for i in range(5, 1000, 5):
  print(i)

for i in range(1, 100):
  if i % 5 == 0:
    print(i)

print(sum([i for i in range(0, 500000) if i % 2 != 0]))

for i in range(2018,0, 4):
  print(i)


lowNum, highNum, mult = 4, 120, 5

for i in range(lowNum, highNum):
  if i % mult == 0:
    print(i)