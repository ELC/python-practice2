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
    numeros_al_final_basico=[]
    lista_letras=[]
    lista_numeros=[]
    for i in lista:
        if type(i) == str:
            lista_letras.append(i)
        else:
            lista_numeros.append(i)
    numeros_al_final_basico.extend(lista_letras)
    numeros_al_final_basico.extend(lista_numeros)
    print(numeros_al_final_basico)

    return numeros_al_final_basico

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
from typing import List, Union

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    
    lista_letras = [i for i in lista if type(i) == str]
    lista_numeros = [i for i in lista if type(i) == int]
    numeros_al_final_comprension = []
    numeros_al_final_comprension.extend(lista_letras)
    numeros_al_final_comprension.extend(lista_numeros)
    print(numeros_al_final_comprension) #Me esta tirando la salida que pide el ejercicio pero el assert me da error

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
