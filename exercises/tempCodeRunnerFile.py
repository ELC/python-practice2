def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """

    lista = [3, "a", 1, "b", 10, "j"]
    numeros_al_final = []

"""
    for x in lista:
        if type(x) == int:
            numeros_al_final.append(x)
        elif type(x)== str:
            numeros_al_final.insert(0,x)

    print (numeros_al_final)
"""

    listaNros = []
    listaLetras = []
    for i in lista:
        if type(i) == str:
            listaLetras.append(i)
        else:
            listaNros.append(i)
    lista = listaLetras + listaNros
    return lista
    print(lista)