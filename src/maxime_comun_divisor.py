"""
El MCD de dos o más números es el producto de todos sus factores primos comunes con las menores potencias con las que aparecen en cada descomposición.
"""

from collections import Counter
from functools import reduce


def prime_factors(n):
   factors = []
   divisor = 2
   while n > 1:
      while n % divisor == 0:
         factors.append(divisor)
         n //= divisor
      divisor += 1
   return factors


def maxime_comun_divisor(numbers):
   # Descomponer cada número en sus factores primos
   prime_factorizations = [Counter(prime_factors(num)) for num in numbers]

   # Encontrar la intersección de los factores primos comunes
   common_factors = reduce(lambda x, y: x & y, prime_factorizations)

   # Calcular el producto de los factores comunes con las menores potencias
   mcd = 1
   for factor, power in common_factors.items():
      mcd *= factor**power

   return mcd