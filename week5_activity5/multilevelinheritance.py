#parent class
class Animal: 

    def __init__(self,name):
     
        self.name=name
        
        
    def display(self):
        return f" Name:{self.name}"
   
# Mammal class inherit Animal class
class Mammal(Animal):
    def __init__(self,name,feature):
        #  It inherits name from Animal.

        super().__init__(name)  #call parent constructor
        self.feature=feature
        
    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    

#Bird class inherit Animal class
class Bird(Animal):
    def __init__(self,name,feature):
        #  It inherits name from Animal.

        super().__init__(name)  #call parent constructor
        self.feature=feature
        
    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    

#Fish class inherit from Animal class
class Fish(Animal):
    def __init__(self,name,feature):
        #  It inherits name from Animal.

        super().__init__(name)  #call parent constructor
        self.feature=feature
        
    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    

#Dog class inherit from Mammal class
#parent class
class Animal: 

    def __init__(self,name):
     
        self.name=name
        
        
    def display(self):
        return f" Name:{self.name}"
   
# Mammal class inherit Animal class
class Mammal(Animal):
    def __init__(self,name,feature):
        #  It inherits name from Animal.

        super().__init__(name)  #call parent constructor
        self.feature=feature
        
    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    

#Bird class inherit Animal class
class Bird(Animal):
    def __init__(self,name,feature):
        #  It inherits name from Animal.

        super().__init__(name)  #call parent constructor
        self.feature=feature
        
    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    

#Dog class inherit from Mammal class
class Dog(Mammal):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Mammal constructor

    def walk(self):
        print(f"{self.name} is walking.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"


#Cat class inherit from Mammal class
class Cat(Mammal):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Mammal constructor

    def walk(self):
        print(f"{self.name} is walking.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"


#Eagle class inherit from Bird class
class Eagle(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Bird constructor

    def fly(self):
        print(f"{self.name} is flying.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"
    



#Penguin class inherit from Bird class
class Penguin(Bird):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Bird constructor

    def fly(self):
        print(f"{self.name} is flying.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"



#Salmon class inherit from Fish class
class Salmom(Fish):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Fish constructor

    def swim(self):
        print(f"{self.name} is flying.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"



#Shark class inherit from Fish class
class Shark(Fish):
    def __init__(self, name, feature):
        super().__init__(name, feature)  # call Fish constructor

    def swim(self):
        print(f"{self.name} is flying.")

    def display(self):
        return f"Name:{self.name}, Feature:{self.feature}"


if __name__ == "__main__":

    animals = [
        Dog("Charlie", "Fur"),
        Eagle("Sky", "Wings"),
        Shark("Jaws", "Fins")
    ]

    # Polymorphism: same method call, different behavior
    for animal in animals:
        print(animal.display())
