# Funtions_Modules

## Script

- `islower.py` Escribe una función: def islower(c):
La función debe devolver True si c es una letra minúscula y False en caso contrario.

- `uppercase.py` Escribe una función:
def uppercase(str):
La función debe imprimir la cadena en mayúsculas seguida de una nueva línea.

- `print_last_digit.py` Escribe una función:
def print_last_digit(number):
La función debe:
Imprimir el último dígito de number.
Devolver el valor del último dígito.

- `pow.py` Escribe una función:
def pow(a, b):
La función debe devolver el valor de a elevado a la potencia de b.
Restricciones:
No está permitido usar el operador de exponente integrado **.
No está permitido importar módulos.
Debes implementar la lógica manualmente usando un bucle.

- `f __name__ == "__main__"` Crea dos archivos:
Archivo: simple_add.py
Define una función add(a, b) que devuelva la suma de dos números.
En el nivel superior del archivo (fuera de cualquier función, pero después de la definición), llama a la función e imprime el resultado de:
add(3, 5)
Archivo: test_import.py
Importa simple_add.
Ejecuta python3 test_import.py
Observa qué ocurre.
Luego modifica simple_add.py:
Mueve la llamada a print dentro de:
  if __name__ == "__main__":
Ejecuta de nuevo.
Debes asegurarte de que:
Al ejecutar python3 simple_add.py, se imprima el resultado.
Al ejecutar python3 test_import.py, no se imprima nada.

- `add.py` Escribe un programa que importe la función add() del archivo add_0.py e imprima el resultado de la suma 1 + 2 = 3

- `calculation.py` Escribe un programa que importe funciones desde calculator_1.py e imprima el resultado de:
suma
resta
multiplicación
división
Usando:
a = 10
b = 5
