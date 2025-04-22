def getFibonacci(quantity: int) -> list[int]:
  """
  Recebe um  valor e retorna a quantidade respectiva de números da sequência de Fibonacci
  """
  values = [1, 1]
  
  for index in range(quantity):
    left = values[index]
    right = values[index + 1]

    current = left + right

    values.append(current)
    
  return values[:quantity]

input = int(input("Digite o tamanho da sequencia que deseja ver: "))
result = getFibonacci(input)
print(f"Resultado: {result}")