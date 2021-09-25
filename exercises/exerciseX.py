###############################################################################


def maximo_recursivo(*args) -> float:
    """Toma una cantidad arbitraria de números y devuelve el mayor.

    Restricciónes:
        - No utilizar la función max
        - No utilizar la ninguna otra función salvo maximo_recursivo
        - Resolver de manera recursiva
    """


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert maximo_recursivo(1, 10, 5, -5) == 10
    assert maximo_recursivo(4, 9, 18, 6) == 18
    assert maximo_recursivo(24, 9, 18, 20) == 24
    assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce  # noqa: E402


def sumatoria_reduce(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar la función reduce.
    Referencia: https://docs.python.org/3/library/functools.html#functools.reduce  # noqa: E501
    """


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN
