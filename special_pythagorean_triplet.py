"""Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


def special_triplet(target_sum):
    a = 1
    b = 1
    while True:
        for b in range(a+1, 500):
            c = target_sum - a - b
            if a + b < c:
                continue
            else:
                if (a**2 + b**2) == c**2:
                    return a*b*c
        a += 1

print(special_triplet(1000))
