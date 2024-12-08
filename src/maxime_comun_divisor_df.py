def maxime_comun_divisor_df(number):
  # Calculamos el MCD iterativamente usando el algoritmo de Euclides
  def gcd(a, b):
    while b != 0:
      a, b = b, a % b
    return a

  # Calculamos el MCD de la lista de números
  mcd = number[0]
  for num in number[1:]:
    mcd = gcd(mcd, num)

  return mcd