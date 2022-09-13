x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1-1
x[1][0] = 15
print(x)
#1-2
students[0]['last_name'] = 'Bryant'
print(students)
#1-3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#1-4
z[0]['y'] = 30

#2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(arr):
  for student in arr:
    # for key,value in student.items():
    #   print(f'{key} - {value}')
    print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students)


#3

def iterateDictionary2(key, list):
  for dict in list:
    print(dict[key])

iterateDictionary2('first_name', students)

#4
def printInfo(dict):
  for key,value in dict.items():
    print( f'{len(value)} {key}')
    for item in value:
      print(item)

dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
