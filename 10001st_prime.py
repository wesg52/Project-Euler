"""Problem 7: 10001st Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import math

def is_prime(num, primes):
    for i in primes:
        if i > math.sqrt(num):
            return True
        if num % i == 0:
            return False
    return True

p_found = 1
st_prime = 10001
prime_list = [2]
num = 1


while p_found != st_prime:
    num += 2
    if is_prime(num, prime_list):
        p_found += 1
        prime_list.append(num)

print(num)
