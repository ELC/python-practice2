"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    vocal = letra.lower()

    if vocal ==  'a':
        return True
    
    if vocal ==  'e':
        return True
    
    if vocal ==  'i':
        return True

    if vocal ==  'o':
        return True

    if vocal ==  'u':
        return True
    
    return False
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns.

    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
assert es_vocal_if("e")
assert es_vocal_if("E")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    vocal = letra.lower()
    if vocal in 'a''e''i''o''u':
        return True
    return False
    """Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
    """
# NO MODIFICAR - FIN
# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    vocal = letra.lower()
    resultado = False
    resultado = vocal in 'a''e''i''o''u'
    return resultado
    

    """Re-escribir como expresión booleana utilizando el operador IN

    Restricciónes:
        - No utilizar IF.
        - Utilizar un único return.
        - No utilizar FOR.
        - No utilizar listas.
    """

print(es_vocal_in("b"))
print(es_vocal_in("a"))
print(es_vocal_in("i"))
print(es_vocal_in("A"))

# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
