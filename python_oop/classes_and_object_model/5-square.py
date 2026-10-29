#!/usr/bin/env python3
"""Defino la clase Square con validación de tamaño."""


class Square:
    """Represento a un cuadrado."""

    def __init__(self, size=0):
        """Inicializo el cuadrado validando su tamaño."""
        self.__size = size

    @property
    def size(self):
        """Devuelvo el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, size):
        """Valido y actualizo el tamaño del cuadrado"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprimo el cuadrado usando el carácter #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
