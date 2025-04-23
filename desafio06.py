def mostComumBird(birds: list[int]) -> int:
  """
  """
  count = {}

  for birdCode in birds:
    if birdCode not in count:
      count[birdCode] = 0
    
    count[birdCode] += 1
  
  result = [None, None]
  
  for item in count:
    if result[0] is None:
        result[0] = item
        result[0] = count[item]
    
    if result[1] > count[item]:
      

print(mostComumBird([1, 1, 2, 2, 3]))