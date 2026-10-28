# classes_and_object_model

Contiene script de clases y objetos y modelos

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
