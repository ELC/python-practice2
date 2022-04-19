"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    total = 0
    for i in range(n+1):
        total += i

    return total
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """

print(sumatoria_basico(5))

# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    return sum(range(n+1))

    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """

print(sumatoria_sum(100))
# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    x=1
    for i in numeros: x = x  * i
    total = 0 if numeros == [] else x 
    return total
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """
print(multiplicar_basico([1, 2, 3, 4]))
print(multiplicar_basico([]))

# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
