## script

- `0-polymorphism_demo.py` introduce los conceptos de herencia y polimorfismo mediante un ejemplo guiado.

- `base_geometry.py` Crea una clase llamada BaseGeometry.
La clase debe incluir los siguientes métodos.
area(self)
Este método representa el área de una figura geométrica.

- `1-rectangle.py` Crea una clase Rectangle que herede de BaseGeometry.
La clase debe representar un rectángulo definido por su ancho y su altura.
Ambos valores deben validarse usando el validador definido en la clase padre.
Instanciación con width y height: def __init__(self, width, height):
width y height deben ser privados. No hay getter ni setter
width y height deben ser enteros positivos, validados por integer_validator
