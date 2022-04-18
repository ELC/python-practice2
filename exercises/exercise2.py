"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad.
"""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    
    maximo = a
    if a<b>c :
        maximo = b
    if a<c>b:
        maximo = c
    
    print(maximo)
    
# NO MODIFICAR - INICIO
assert maximo_encadenado(10, 1, 5) == 10
assert maximo_encadenado(5, 10, 1) == 10
assert maximo_encadenado(5, 10, 5) == 10

assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(9, 4, 18) == 18
assert maximo_encadenado(9, 9, 18) == 18

assert maximo_encadenado(24, 9, 18) == 24
assert maximo_encadenado(24, 18, 9) == 24
assert maximo_encadenado(24, 18, 18) == 24
# NO MODIFICAR - FIN


###############################################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:

    maximo = max(a,b,c,d)
    print(maximo)


maximo_cuadruple(1, 10, 5, -5) == 10
maximo_cuadruple(4, 9, 18, 6) == 18
maximo_cuadruple(24, 9, 18, 20) == 24
maximo_cuadruple(24, 9, 18, 30) == 30


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_arbitrario(*args) -> float:
    print(max(args))
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists # noqa: E501
    """


# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
