"""Type, Comprensión de Listas, Sorted y Filter."""

from os import listxattr
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    lista_a = []
    lista_b = []
    for i in lista:
        if type(i) == type(1):
            lista_b.append(i)

        if type(i) == type(''):
            lista_a.append(i)

    return lista_a +lista_b
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
print(numeros_al_final_basico([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################

from typing import List, Union

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    
    lista_a = [i for i in lista if type('') == type(i)]
    lista_b = [i for i in lista if type(1) == type(i)]
    return lista_a +lista_b

    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
