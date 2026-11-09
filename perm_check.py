def solution(A):
  #stores number that have already been seen and appeared
  seen = set()
  for number in A:
    #numbers in the permutation must be between 1 and the length of A
    if number < 1 or number > len(A):
      return 0
    #permutation cannot contain duplicates
    if number in seen:
      return 0
    seen.add(number)

  return 1
