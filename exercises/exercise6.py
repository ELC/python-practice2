"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


lista=[3, "a", 1, "b", 10, "j"]
def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    lista1=[]
    for i in lista:                            
        if type(i) == int:
            lista1.append(i)
        elif type(i)== str:                 
            lista1.insert(0,i)
    print(lista1)
    return lista1

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501

# NO MODIFICAR - FIN


###############################################################################

#DIAPO 12 funciones
from typing import List, Union
def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """

    numeros=[]
    letras=[]
    lista = [i for i in lista if type(i) ==int]
    lista = [i for i in lista if type(i) == str]
    suma = letras + numeros
    print(suma)
# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
