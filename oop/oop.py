class Animal :
    def __init__(self,name,color,age,size):
          self.name=name
          self.color=color
          self.age=age
          self.size=size
          
    def print_all(self):
          print(self.name)
          print(self.color)
          print(self.age)
          print(self.size)
         
    def eat(self,food):
          print(self.name, "is eating",food)
    def sleep(self):
          print(self.name, "is sleeping")
    def breathe(self):
          print(self.name, "is breathing")         
          
Dog=Animal(name="sasha",color="black",age=4,size="huge")
Cat=Animal(name="lulu",color="white",age=2,size="tiny")

Dog.eat(food="pizza")
Cat.eat(food="fish")
Dog.print_all()
Cat.print_all()


