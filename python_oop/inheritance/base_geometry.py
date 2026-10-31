#!/usr/bin/env python3
"""Defino la clase base para figuras geométricas."""


class BaseGeometry:
    """Represento la geometría básica."""

    def area(self):
        """Indico que el cálculo del área no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valido que un valor sea un entero positivo."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
