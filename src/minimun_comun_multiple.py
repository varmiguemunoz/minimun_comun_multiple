"""
El MCM de dos o más números es el producto de todos los factores primos que aparecen en cualquier descomposición, cada uno elevado a la mayor potencia con la que aparece en las descomposiciones.
"""
from functools import reduce


def factores_primos(n):
    factores = {}
    divisor = 2
    while divisor <= n:
        while n % divisor == 0:
            if divisor not in factores:
                factores[divisor] = 0
            factores[divisor] += 1
            n //= divisor
        divisor += 1
    return factores


def minimo_comun_multiple(a, b):
    factores_a = factores_primos(a)
    factores_b = factores_primos(b)

    mcm_factores = {}

    for factor in set(factores_a.keys()).union(factores_b.keys()):
        mcm_factores[factor] = max(factores_a.get(factor, 0),
                                   factores_b.get(factor, 0))

    # Calculamos el MCM multiplicando los factores elevados a sus mayores exponentes
    mcm = 1
    for factor, exponente in mcm_factores.items():
        mcm *= factor**exponente

    return mcm


def minimun_comun_multiple_list(numbers):
    return reduce(minimo_comun_multiple, numbers)
