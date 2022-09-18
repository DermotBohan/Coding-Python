def main():
  x = 5 # integers are immutable, cannot be changed.
  y = x
  y = 3

  print(type(x))
  print(type(y))
  print(id(x))
  print(id(y))
  print(x)
  print(y)
  main2()

def main2():
  print('main2()')
  x = [5] # list - is mutable: can be changed
  y = x
  y[0] = 3

  print(type(x))
  print(type(y))
  print(id(x))
  print(id(y))
  print(x)
  print(y)



if __name__ == '__main__': main()

  
