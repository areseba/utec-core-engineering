#!/usr/bin/env python3
"""Modulo para agregar texto."""


def append_write(filename="", text=""):
    """Agrego el texto con formato utf-8 y cuento los caracteres."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
