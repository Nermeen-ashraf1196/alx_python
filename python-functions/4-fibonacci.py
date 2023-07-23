def fibonacci_sequence(n):
 # Returns a list of the first n Fibonacci numbers.
    sequence = [0, 1] 
 # first loop (if-else loop)
    if n <= 1:
        return sequence[:n ]
    else:
 # second loop (while loop)
        while len(sequence) <= n-1:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence