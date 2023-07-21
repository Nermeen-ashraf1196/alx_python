def is_prime(number):
 # Returns True if the number is prime, and False otherwise.
 # If given number is greater than 1
    if number > 1:
     # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
         # If num is divisible by any number between
         # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return(False)
            else:
                return(True)
    else:
        return(False)