# core_data_structures

Contiene Script de Python

## Script

- `print_list_integer.py` Escribe una función que imprima todos los enteros de una lista.
Prototipo: def print_list_integer(my_list=[])
Formato: un entero por línea
Puedes asumir que cada elemento de my_list es un entero.

- `element_at.py` Escribe una función que recupere un elemento de una lista como en C.
Prototipo: def element_at(my_list, idx):
Si idx es negativo o está fuera de rango, devuelve None.
En caso contrario, devuelve el elemento en la posición idx.

- `replace_in_list.py` Escribe una función que reemplace un elemento de una lista en una posición específica.
Prototipo: def replace_in_list(my_list, idx, element):
Si idx es negativo o está fuera de rango, devuelve la lista original sin cambios.
En caso contrario, reemplaza el elemento en la posición idx por element y devuelve la lista.

- `print_matrix_integer.py` Escribe una función que imprima una matriz de enteros.
Prototipo: def print_matrix_integer(matrix=[[]]):
matrix es una lista de listas (lista 2D).
Formatea cada fila en su propia línea.
Los valores de una fila deben estar separados por un solo espacio.

- `add_tuple.py` Escribe una función que sume dos tuplas.
Prototipo: def add_tuple(tuple_a=(), tuple_b=()):
Devuelve una nueva tupla con exactamente dos enteros.
Trata los valores faltantes como 0.
Ignora los valores más allá de los dos primeros.

- `common_elements.py` Escribe una función que devuelva un conjunto de elementos comunes en dos conjuntos.
Prototipo: def common_elements(set_1, set_2):
Devuelve un nuevo conjunto que contenga solo los elementos presentes en set_1 y set_2.

- `update_dictionary.py` Escribe una función que reemplace o agregue un par clave/valor en un diccionario.
Prototipo: def update_dictionary(a_dictionary, key, value):
Si key ya existe, reemplaza su valor.
Si key no existe, créala.
Devuelve el diccionario (actualizado).

- `best_score.py` Escribe una función que devuelva la clave con el valor entero más grande.
Prototipo: def best_score(a_dictionary):
Puedes asumir que todos los valores son enteros.
Si a_dictionary es None o está vacío, devuelve None.
Puedes asumir que todos los valores son diferentes.
