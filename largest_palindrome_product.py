# -*- coding: utf-8 -*-
"""Problem 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

num1 = 999
num2 = 999

largest_product = 999 * 999
largest_drome = 0

while largest_drome <= largest_product:
    largest_product = num1 * num2
    while num2 > 1:
        cand = num1 * num2
        if cand == int(str(cand)[::-1]):
            if cand > largest_drome:
                largest_drome = cand
        num2 -= 1
    num1 -= 1
    num2 = num1

print(largest_drome)
