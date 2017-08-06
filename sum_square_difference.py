# -*- coding: utf-8 -*-
"""Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sum_of_square(num):
    total = 0
    for i in range(1, num+1):
        total += i**2
    return total

def square_of_sum(num):
    sum_total = 0
    for i in range(1, num+1):
        sum_total += i
    return sum_total**2

print(square_of_sum(100) - sum_of_square(100))
