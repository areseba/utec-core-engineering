## script

- `0-square.py` Define una clase llamada Square que represente un cuadrado.

- `1-square.py` Define una clase Square con:
un atributo de instancia privado size
El tamaño debe establecerse cuando se crea el objeto.

- `2-square.py` Agrega validaciones al atributo size en la clase Square.

El atributo size debe cumplir con lo siguiente:
debe ser un entero. De lo contrario, lanza una excepción TypeError con el mensaje size must be an integer
debe ser mayor o igual que 0. De lo contrario, lanza una excepción ValueError con el mensaje size must be >= 0

- `3-square.py` Agrega un método de instancia area(self) a la clase Square que devuelva el área del cuadrado según la longitud de su side.

- `4-square.py` Añade getters y setters para el atributo size.

El setter debe validar la entrada usando las mismas reglas que antes.

- `5-square.py` Agregua un método de instancia público def my_print(self) que imprima en stdout el cuadrado con el carácter #
Si size es igual a 0, imprime una línea vacía.

- `6-square.py` Agrega e implementa el método especial:
__str__()
Atributo de instancia privado: position:
propiedad def position(self): para recuperarlo
setter de propiedad def position(self, value): para establecerlo:
position debe ser una tupla de 2 enteros positivos, de lo contrario lanza una excepción TypeError con el mensaje position must be a tuple of 2 positive integer
Instanciación con size opcional y position opcional: def __init__(self, size=0, position=(0, 0)):
Método público de instancia: def my_print(self): que imprime en stdout el cuadrado con el carácter #:
si size es igual a 0, imprime una línea vacía
position debe usarse mediante espacios
Imprimir una instancia de Square debe tener el mismo comportamiento que my_print()

- `1-rectangle.py` Define una clase Rectangle con:
Atributo de instancia privado width:
propiedad width(self) para recuperarlo
setter de propiedad width(self, value) para asignarlo.
width debe ser un entero; de lo contrario, lanza una excepción TypeError con el mensaje width must be an integer
si width es menor que 0, lanza una excepción ValueError con el mensaje width must be >= 0
Atributo de instancia privado height:
propiedad height(self) para recuperarlo
setter de propiedad height(self, value) para asignarlo
height debe ser un entero; de lo contrario, lanza una excepción TypeError con el mensaje height must be an integer
si height es menor que 0, lanza una excepción ValueError con el mensaje height must be >= 0
Instanciación con width y height opcionales y valor por defecto de 0. (__init__(self, width=0, height=0))

- `2-rectangle.py` Agrega los siguientes métodos de instancia a la clase Rectangle:
area() que devuelve el área del rectángulo
perimeter() que devuelve el perímetro del rectángulo:
si width o height es igual a 0, el perímetro es igual a 0
