

def isAnagrama(word1: str,word2: str) -> bool:
  """
  Retorna se as palavras fornecidas são anagramas
  """

  firstWord = list(word1)
  secondWord = list(word2)

  firstWord.sort()
  secondWord.sort()

  firstWord = "".join(firstWord)
  secondWord = "".join(secondWord)

  return firstWord == secondWord

word = input("Digite uma palavra: ")
word2 = input("Digite outra palavra: ")

result = f"'{word}' é um anagrama de '{word2}'" if isAnagrama(word,word2) else f"'{word}' não é um anagrama de '{word2}'"
print(f"Resultado: {result}")