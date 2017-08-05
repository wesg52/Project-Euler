"""Problem 2: Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def yield_fib_num(up_to):
    fib_terms = (1,1)
    yield 1
    while fib_terms[0] + fib_terms[1] <= up_to:
        new_term = fib_terms[0] + fib_terms[1]
        fib_terms = (fib_terms[1], new_term)
        yield new_term

def total_even_sum(up_to):
    total = 0
    fib_sequence = yield_fib_num(up_to)
    for i in fib_sequence:
        if i % 2 == 0:
            total += i
    return total

print(total_even_sum(4000000))