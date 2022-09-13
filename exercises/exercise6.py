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


# NO MODIFICAR - INICIO
    
    cadenas=[]
    numeros=[]
    for i in lista:
        if type(i) is int:
           numeros.append(i)
        else:
            cadenas.append(i)
    cadenas.extend(numeros)
    return cadenas



assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """


# NO MODIFICAR - INICIO

    lista_str=[]
    lista_int=[]
    lista_str=[elemento for elemento in lista if type(elemento) is str]
    lista_int=[elemento for elemento in lista if type(elemento) is int]
    lista_str.extend(lista_int)
    return lista_str

assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
