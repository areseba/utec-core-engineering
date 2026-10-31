#!/usr/bin/env python3
"""Defino la clase Square."""

Rectangle = __import__('2-rectangle').Rectangle
"""Obtengo la clase Rectangle del archivo rectangle.py"""


class Square(Rectangle):
    """Represento un cuadrado."""

    def __init__(self, size):
        """Inicializo un cuadrado con un tamaño validado."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
