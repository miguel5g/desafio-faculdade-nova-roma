def fatorial(value: int) -> int:
  """
  Recebe value e retorna o fatorial dele
  """
  if value < 1:
    return 1
  else:
    return value * fatorial(value - 1)

input = int(input("Digite um número para ver o fatorial: "))
result = fatorial(input)
print(f"Resultado: {result}")