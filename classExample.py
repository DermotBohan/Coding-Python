class Duck:

  sound = 'Quaaaaack!'
  movement = 'Walks like a duck.'

  def quack(self):
    print(self.sound)

  def walk(self):
    print(self.movement)

def main():
  donald = Duck()
  donald.quack()
  donald.walk()

if __name__== '__main__': main()
