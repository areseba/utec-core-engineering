#!/usr/bin/env python3
"""Define la clase Square con su representación en texto."""

Rectangle = __import__('1-square').Square
"""Obtengo la clase Rectangle del archivo rectangle.py"""


class Square(Rectangle):
    """Representa un cuadrado."""

    def __str__(self):
        """Devuelvo la descripción del cuadrado."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
