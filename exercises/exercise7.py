"""Any y Sets."""

from typing import Any, Iterable
test_list = [1, "hello", 35.20]

def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:  # noqa: E501

    for i in lista_1:
        for j in lista_2:
            if i == j:
                return True

    return False
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricciones:
        - Utilizar dos bucles FOR anidados.
        - Utilizar dos returns.
    """

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
from typing import Any, Iterable
test_list = [1, "hello", 35.20]

def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for i in lista_1:
        if i in lista_2:
            return True
    
    return False
    """Re-Escribir utilizando un sólo bucle y el operador IN.

    Restricciones:
        - Utilizar un único bucle FOR.
        - Utilizar dos returns.
    """

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
from typing import Any, Iterable
test_list = [1, "hello", 35.20]

def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    
    return any([x for x in lista_1 if (j for j in lista_2 if j == x)])
    
    """Re-Escribir utilizando la funcion any.

    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea.

    Referencia: https://docs.python.org/3/library/functions.html#any
    """

print(not superposicion_any(test_list, (2, "world", 35.20)))
#==============================================================================
# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
from typing import Any, Iterable
test_list = [1, "hello", 35.20]

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:

    resultado = set(lista_1).isdisjoint(set(lista_2))
    return not resultado
   
    """Re-Escribir utilizando conjuntos (sets).
    if resultado != {}:
            return True
    Restricciones:
        - Resolver sólo utilizando operaciones de conjuntos
        - No utilizar ANY, ALL, FOR, IF ni COMPRENSIONES

    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset  # noqa: E501
    """
print(not superposicion_set(test_list, (2, "world", 35.85)))
print(superposicion_set(test_list, (2, "world", 35.20)))

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
