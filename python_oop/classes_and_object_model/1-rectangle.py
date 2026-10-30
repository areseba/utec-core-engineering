#!/usr/bin/env python3
"""Defino la clase Rectangle con validación de ancho y alto."""


class Rectangle:
    """Represento a un rectangulo."""

    def __init__(self, width=0, height=0):
        """Inicializo el rectangulo con ancho y alto."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelvo el ancho del rectangulo."""
        return self.__width

    @property
    def height(self):
        """Devuelvo la altura del rectangulo."""
        return self.__height

    @width.setter
    def width(self, value):
        """Valido y actualizo el ancho del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Valido y actualizo elalto del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
