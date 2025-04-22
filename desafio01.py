def fatorial(valor: int) -> int:
  """
  Recebe valor e retorna o fatorial dele
  """
  if valor < 1:
    return 1
  else:
    return valor * fatorial(valor - 1)

entrada = int(input("Digite um número para ver o fatorial: "))
resultado = fatorial(entrada)
print(f"Resultado: {resultado}")