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
    if isinstance(obj, Quacker):
        return True
    return False


Quacker.register(Duck)
duck = Duck()
cat = Cat()

print(is_a_quacker(duck))
print(is_a_quacker(cat))
print(issubclass(Duck, Quacker))
print(issubclass(Cat, Quacker))