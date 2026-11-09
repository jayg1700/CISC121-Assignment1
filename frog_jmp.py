def solution(X, Y, D):
    #Find distance frog needs to travel
    distance = Y - X
    #count how many FULL jumps fit into that set distance
    jumps = distance // D
    #If any distance is left over, one more jump is required
    if distance % D != 0:
      jumps = jumps + 1

    return jumps
