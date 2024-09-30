
#Calculator with four functions/methods


def greet(name):
    return f"Hello, {name}"


print(greet("Alice"))


def add_numbers(a,b):
    return a + b



result = add_numbers(5,7)
print(result)


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", greeting="Hi"))

add = lambda x, y: x + y
print(add(3,4))


class Dog: 
    species = "Canis lupus familiaris" # Class attribute
    
    def __init__(cls, name):
        cls.name = name
        
    def bark(cls):
        return f"{cls.name} says woof!"
    
    @classmethod
    def get_species(cls):
        return cls.species

# class method
print(Dog.get_species()) 
    
my_dog = Dog("Buddy")
print(my_dog.bark())


#finish attributes and methodes sum, subtract etc....

# calculator.py

# calculator.py

class Calculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def multiply(self):
        return self.number_1 * self.number_2
    
    def add(self):
        return self.number_1 + self.number_2
    
    def subtract(self):
        return self.number_1 - self.number_2
    
    def divide(self):
        if self.number_2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.number_1 / self.number_2

   
        
        


