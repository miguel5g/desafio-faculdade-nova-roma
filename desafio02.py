def isPalindrome(word: str) -> bool:
  """
  Retorna se a palavra fornecida é um palíndromo
  """
  result = True
  
  for index in range(len(word)):
    char = word[index]
    endIndex = len(word) - 1 - index
    inverseChar = word[endIndex]

    if char != inverseChar:
      result = False
    
  return result

input = input("Digite uma palavra para saber se é palíndromo: ")
result = "Sim" if isPalindrome(input) else "Não"
print(f"Resultado: {result}")