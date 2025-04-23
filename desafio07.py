def roundGrade(grade: int) -> int:
  """
  Recebe uma nota e arredonda a mesma de acordo com os critérios escolhidos
  """
  if grade < 40: return grade

  nextMultiple = (grade - grade % 5) + 5
  difference = nextMultiple - grade

  return nextMultiple if difference < 3 else grade

def roundGrades(grades: list[int]) -> list[int]:
  """
  Recebe um array de notas e arredonda as notas de acordo com os critérios escolhidos
  """
  return [roundGrade(grade) for grade in grades]

input = int(input("Digite a nota do aluno: "))
result = roundGrades([84, 29, 56])
print(f"Resultado: {result}")