
def a():
    return 5
print(a())
#5

def a():
    return 5
print(a()+a())
#10

def a():
    return 5
    return 10
print(a())
#5


def a():
    return 5
    print(10)
print(a())
#5

def a():
    print(5)
x = a()
print(x)

#none


def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# no return value so there's type error when concatenating the function calls that return none


def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#"25"

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# 10


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#7
#14
#21

def a(b,c):
    return b+c
    return 10
print(a(3,5))
#8


b = 500
print(b)
#500
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# 500  300 500


b = 500
print(b)
#500
def a():
    b = 300
    print(b)
    return b
print(b)
#500
a()
print(b)
#500 300 when calling a func

b = 500
print(b)
#500
def a():
    b = 300
    print(b)
    return b
print(b)
#500
b=a()
print(b)
#300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#1, undefined
#1, undefined

def a():
    print(1)
    x = b()
    print(x)
    return 10

def b():
    print(3)
    return 5
y = a()

print(y)

#1 3 10
