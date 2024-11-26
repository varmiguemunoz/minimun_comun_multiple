"""
El MCD de dos o más números es el producto de todos sus factores primos comunes con las menores potencias con las que aparecen en cada descomposición.
"""

from math import gcd
from functools import reduce


def maxime_comun_divisor(number):
   return reduce(gcd, number)
