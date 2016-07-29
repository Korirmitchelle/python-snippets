def tribonacci(n):
    nextNum = 0
    sequence = [0, 1, 2]
    while nextNum < n:
        nextNum = int(sequence[len(sequence)-3]) + int(sequence[len(sequence)-2]) + int(sequence[len(sequence)-1])
        if nextNum < n:
            sequence.append(nextNum)
    return sequence


#print tribonacci(20)