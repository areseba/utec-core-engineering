#!/usr/bin/env python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    mejor_clave = None
    mayor_puntuacion = None
    for clave in a_dictionary:
        if mayor_puntuacion is None or a_dictionary[clave] > mayor_puntuacion:
            mayor_puntuacion = a_dictionary[clave]
            mejor_clave = clave
    return mejor_clave
