from abc import ABC, abstractmethod

class Quacker(ABC):
    @abstractmethod
    def quack(self):
        pass

class Duck:
    def quack(self):
        return "Quack!"

class Cat:
    def quack(self):
        return "Meow!"

def is_a_quacker(obj):
    if type(obj) is Quacker:
        return True
    return False

Quacker.register(Duck) # the duck class will use the Quacker's abstract method

duck = Duck()
cat = Cat()

print(is_a_quacker(duck))
print(is_a_quacker(cat))
print(issubclass(Duck, Quacker)) #True
print(issubclass(Cat, Quacker))


