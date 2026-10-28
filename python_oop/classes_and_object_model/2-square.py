#!/usr/bin/env python3
"""Defino la clase Square con validación de tamaño."""


class Square:
    """Represento a un cuadrado."""

    def __init__(self, size=0):
        """Inicializo el cuadrado validando su tamaño."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
