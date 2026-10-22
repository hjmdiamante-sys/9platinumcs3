#creates parent class Animal
class Animal: 
  def __init__(self, name): #constructor that initializes the name
    self.name = name 

  def eat(self): #eat() method
    print(f"{self.name} eats something.") 

  def make_sound(self):  #make_sound() method
    print(f"{self.name} makes a sound!") 

#creates child class Elephant
class Elephant(Animal):  
  def eat(self): #overrides the method eat() (wow, method overriding)
    print(f"{self.name} eats grass and fruits.") 

  def make_sound(self):  #overrides the method make_sound() 
    print(f"{self.name} trumpets!") 
    
#creates child class Lion
class Lion(Animal): 
  def eat(self):
    print(f"{self.name} eats fresh meat.") 

  def make_sound(self): 
    print(f"{self.name} roars loudly!") 
    
#creates child class Monkey
class Monkey(Animal): 
  def eat(self):
    print(f"{self.name} eats bananas.") 

  def make_sound(self): 
    print(f"{self.name} chatters!") 

#objects
lion = Lion("Simba") 
elephant = Elephant("Dumbo") 
monkey = Monkey("George") 

animals = [lion, elephant, monkey] #putting all the the objects in one list called animals

for animal in animals: #for loop to cycle all items in the list
  animal.make_sound()
  animal.eat()
  print("-----") #found in the output 
  
