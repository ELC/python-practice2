"""Tuple, Enumerate, Zip, Args.


Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""


from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    aux = []
    for i in range(len(nombres)):
        aux = aux + [nombres[i],precios[i]]
    
    return tuple(aux)


    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción:
        - Utilizar un bucle FOR.
        - Utilizar la función range.
        - Utilizar índices.
    """

print(combinar_basico(nombre_articulos, precio_articulos))
# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


from typing import Any, List, Tuple
id_articulos = [6852, 1459, 3578]
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]

def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    
    lista_1 = tuple(enumerate(nombres))
    lista_2 = tuple(enumerate(precios))
    lista_3 = tuple(enumerate(ids))
    j = 0
    final= []
    for i in nombres:
        aux = tuple([lista_1[j][1],lista_2[j][1],lista_3[j][1]])
        final.append(aux)
        j= j+1

    return tuple(final)
    """Re-Escribir utilizando enumerate y agregando un nuevo componente.
    Restricción:
        - Utilizar un bucle FOR.
        - No Utilizar la función range.
        - No Utilizar la función zip.
    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """
# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


from typing import Any, List, Tuple
id_articulos = [6852, 1459, 3578]
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501


    aux = zip(nombres,precios,ids)
    return tuple(aux)

"""Re-Escribir utilizando zip.

Restricción:
    - Utilizar un bucle FOR.
    - No utilizar la función range.
    - No utilizar la función enumerate.
    - No utilizar índices.
Referencia: https://docs.python.org/3/library/functions.html#zip
"""


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################

from typing import Any, List, Tuple
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]
id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]

def combinar_zip_args(*args) -> Tuple[Any]:

    final = zip(*args)
    return tuple(final)
    """Re-Escribir utilizando zip y una cantidad arbitraria de componentes.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices.

    Referencia: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists  # noqa: E501
    """

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
# NO MODIFICAR - FIN
