"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad.
"""


from ast import arg
from this import d


def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.

    Restricciones:
        - Utilizar comparaciones encadenadas.
        - Utilizar UNICAMENTE dos IFs
        - No utilizar ELSE
        - No utilizar AND, OR o NOT

    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons # noqa: E501
    """

    if b < a > c:
        return a
    if a < b > c:
        return b
    return c


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
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
    """Re-escribir para que tome 4 parámetros, utilizar la función max.

    Referencia: https://docs.python.org/3/library/functions.html#max"""

    resultado = max(a, b, c, d)
    return resultado


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_arbitrario(*args) -> float:
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists # noqa: E501
    """

    resultado = max(*args)
    return resultado


# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
