"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501

    if multiplicar:
        total = a*b
    elif b == 0:
        total = "Operación no válida"
    else:
        total = a/b

    return total
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - Utilizar IF con ELIF con ELSE.
        - No utilizar AND ni OR.
    """

# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN


###############################################################################
from typing import Union

def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501

    if multiplicar:
        return a*b
    if b == 0:
        return 'Operacion no válida'
    
    return a/b


print(operacion_multiple(1, 1, True))
print(operacion_multiple(1, 1, False))
print(operacion_multiple(25, 5, True) )
print(operacion_multiple(25, 5, False))
print(operacion_multiple(0, 5, True))
print(operacion_multiple(0, 5, False))
print(operacion_multiple(1, 0, True))
print(operacion_multiple(1, 0, False))
# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN
