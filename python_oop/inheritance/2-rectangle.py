#!/usr/bin/env python3
"""Defino la clase Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry
"""Obtengo la clase BaseGeometry del archivo base_geometry.py"""


class Rectangle(BaseGeometry):
    """Representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa un rectángulo validando sus dimensiones."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripción del rectángulo."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
