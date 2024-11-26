"""
En esta actividad, deberás desarrollar un programa que calcule el mínimo común múltiplo (MCM) y el máximo común divisor (MCD) de tres o más números enteros positivos. El programa debe permitir la entrada de estos números y luego realizar los cálculos necesarios para obtener el MCM y el MCD.
"""

from src.maxime_comun_divisor import maxime_comun_divisor
from src.minimun_comun_multiple import minimun_comun_multiple_list


def main():
  user_number = input(
      "Ingrese los número a calcular separados por espacios: ").strip()

  numbers = user_number.split()

  try:
    numbers = [int(num) for num in numbers]
  except ValueError:
    print("Todos los valores deben ser enteros positivos.")
    return

  # Verificamos que cada número sea positivo y tenga al menos 3 cifras
  if any(num < 100 for num in numbers):
    print("Cada número debe tener al menos 3 cifras y ser positivo.")
    return

  # Calculamos el MCD de la lista de números
  mcd = maxime_comun_divisor(numbers)
  mcm = minimun_comun_multiple_list(numbers)

  print("El maximo comun divisor es: ", mcd)
  print("El minimo comun multiplo es: ", mcm)


if __name__ == "__main__":
  main()
