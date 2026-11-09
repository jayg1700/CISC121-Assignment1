def solution(A):
  #Stores numbers that don't have a matching pair as of yet
  unpaired = set()

  for number in A:
    #if matching number is found, remove from set
    if number in unpaired:
      unpaired.remove(number)
    else:
      #if the number has no match
      unpaired.add(number)

  return unpaired.pop()
