import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if int(last_digit_str) > 5:
    print (f"Last digit of {number} is {last_digit}","and is greater than 5")
elif int(last_digit_str) == 0:
    print(f"Last digit of {number} is {last_digit}","is Zero")
else:
    print(f"Last digit of {number} is {last_digit}","and is less than 6 and not 0")