"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    lista_main = []
    lista_numeros = []
    lista_letras = []

    for element in lista:
        if type(element) == str:
            lista_letras.append(element)
        else:
            lista_numeros.append(element)

    lista_main.extend(lista_letras)
    lista_main.extend(lista_numeros)
    return lista_main


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    lista_main = []
    lista_numeros = [elemento for elemento in lista if type(elemento) == str] # Use bucle acá, existe otra forma ?
    lista_letras = [elemento for elemento in lista if type(elemento) == int]

    lista_main.extend(lista_numeros)
    lista_main.extend(lista_letras)

    return lista_main


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
