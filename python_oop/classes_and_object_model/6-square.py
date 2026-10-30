#!/usr/bin/env python3
"""Defino la clase Square con validación de tamaño."""


class Square:
    """Represento a un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializo el cuadrado validando su tamaño."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelvo el tamaño del cuadrado."""
        return self.__size

    @property
    def position(self):
        """Devuelvo la posicion del cuadrado."""
        return self.__position

    @size.setter
    def size(self, size):
        """Valido y actualizo el tamaño del cuadrado"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        """Valido y actualizo la posición del cuadrado."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) and n >= 0 for n in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprimo el cuadrado respetando su posición."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelvo el cuadrado como una cadena."""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
