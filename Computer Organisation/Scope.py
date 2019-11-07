a = 10
b = 20
c = 30
def foo1(a, b):
  a = b + c
  print(a)
  return a

def foo2(b, c):
  b = a + c
  print(b)
  return b

def foo3(a, c):
  c = a + b
  print(c)
  return c

foo1(3,4)
foo2(5,6)
foo3(7,8)
#foo2(foo1(1, 2), foo2(1, 2))
foo2(32,12)
#foo2(foo2(3, 4), foo3(2, 9))
foo2(14,22)


def add(num1, num2):
  return num1 + num2

def triple(num):
  return add(num, add(num, num))
def quadruple(num):
    return add(num, add(num, add(num,num)))