def solution(A, K):
  #If array is empty, then there isn't anything to rotate
  if len(A) == 0:
    return A

  #Rotate array K times, remove last element, then insert it at the beginning
  for i in range(K):
    last = A.pop()
    A.insert(0, last)

  return A
