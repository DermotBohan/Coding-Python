def fun1(x):
  print('fun1 Receives: ', end = ' ')
  print(x)
  x = 'fun'
  print('fun1 Returns: ', end = ' ')
  print(x)
  # if return is commented out, main receives none
  # return x







def main():
  x = 'mainVariable'
  print("START", end = ' ')
  print(x)

  x = fun1(x)
  #fun1(x)

  print("Post Function: ", end = ' ')
  print(x)







if __name__ == '__main__': main()
