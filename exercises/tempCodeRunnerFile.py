numeros = [1, 2, 3, 4, 5, 6]
numeros_al_cubo = list(map(lambda numeros : pow(numeros,3) ,numeros))
#=====================================

#=====================================
"""
Escribir una función lambda que permita filtrar todos los elementos pares

Restricción: Utilizar List, filter, lambda y la variable numeros_al_cubo
"""
numeros_al_cubo_pares = list(filter( lambda numeros : pow(numeros,3)%2 == 0,numeros_al_cubo))
print(numeros_al_cubo_pares)
#=====================================

#=====================================
"""
Escribir una función Lambda que sume todos los elementos

Restricción: Utilizar reduce, lambda y la variable numeros_al_cubo_pares
"""

from functools import reduce  # noqa: E402

suma_numeros_al_cubo_pares =  reduce(lambda a,b:a+b,numeros_al_cubo_pares)


# NO MODIFICAR - INICIO
assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288