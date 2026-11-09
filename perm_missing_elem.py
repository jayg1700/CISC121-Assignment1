def solution(A):
  #sum of all numbers that should be there
  expected_sum = sum(range(1, len(A) + 2))
  #sum of all numbers that are actually in array
  actual_sum = sum(A)
  #missing number is the difference between expected and actual
  missing = expected_sum - actual_sum

  return missing
