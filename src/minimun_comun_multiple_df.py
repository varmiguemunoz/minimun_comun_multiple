def minimun_comun_multiple_df(numbers):
  # Calculamos el MCD usando el algoritmo de Euclides
  def gcd(a, b):
    while b != 0:
      a, b = b, a % b
    return a

  # Calculamos el MCM de dos números basado en el MCD
  def lcm(a, b):
    return abs(a * b) // gcd(a, b)

  # Iteramos sobre la lista de números para calcular el LCM acumulativamente
  mcm = numbers[0]
  for num in numbers[1:]:
    mcm = lcm(mcm, num)

  return mcm