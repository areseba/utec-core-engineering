#!/usr/bin/env python3

class Animal:
    """Representa un animal."""

    def speak(self):
        """Devuelve un sonido genérico."""
        return "Some sound"


class Dog(Animal):
    """Representa un perro."""
    pass


class Cat(Animal):
    """Representa un gato."""
    pass


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())