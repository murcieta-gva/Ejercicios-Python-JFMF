# This Python file uses the following encoding: utf-8
import os, sys

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio2b

def test_esMayorEdad():
    assert ejercicio2b.esMayorEdad(5,'Jose') == False
    assert ejercicio2b.esMayorEdad(18,'Paula') == True
    assert ejercicio2b.esMayorEdad(21,'Laura') == True
