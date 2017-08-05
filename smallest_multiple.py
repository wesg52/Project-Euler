"""Problem 5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
num = 0
while True:
    num += 19
    i = 1
    for i in range(1,21):
        if num % i != 0:
            break
    if i == 20:
        print(num)
        break
