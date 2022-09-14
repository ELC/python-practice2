"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - Utilizar IF con ELIF con ELSE.
        - No utilizar AND ni OR.
    """
    if multiplicar == True:
        resultado = a*b
    elif b == 0:
        resultado = "Operación no válida"
    else:
        resultado = a/b
    return resultado


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


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:  # noqa: E501
    """Re-Escribir el ejercicio anterior utilizando tres returns.

    Restricciones:
        - Utilizar 2 IF.
        - No Utilizar IF anidados.
        - No utilizar ELIF ni ELSE.
        - No utilizar AND ni OR."""
    if multiplicar == True:
        return a*b
    if b == 0:
        return "Operación no válida"
    return a/b


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
