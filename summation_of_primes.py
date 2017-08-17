"""Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import math

def is_prime(num):
    for f in range(3, int(round(math.sqrt(num)))+1):
        if num % f == 0:
            return False
    return True

total_sum = 2
for i in range(3, 2000000, 2):
    if is_prime(i):
        total_sum += i

print(total_sum)
