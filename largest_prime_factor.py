"""Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import math

num = 600851475143

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 2):
        if x % i == 0:
            return False
    return True

prime = 2
while num != 1:
    while num % prime == 0:
        num /= prime
    if num == 1:
        print(prime)
    if prime != 2:
        prime_cand = prime + 2
        while is_prime(prime_cand)  == False:
            prime_cand += 2
        prime = prime_cand
    else:
        prime += 1
