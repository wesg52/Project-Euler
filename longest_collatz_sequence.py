"""
Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
 Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

def next_collatz_num(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

seq_dict = {1:1, 2:2}

for i in range(3, 1000001):
    chain_len = 1
    seq_head = i
    while seq_head not in seq_dict:
        seq_head = next_collatz_num(seq_head)
        chain_len += 1
    total_len = chain_len + seq_dict[seq_head]
    seq_dict[i] = total_len

max_chain_num = 0
max_chain_len = 0

for key, value in seq_dict.items():
    if value > max_chain_len:
        max_chain_num = key
        max_chain_len = value
print('Max length chain is', str(max_chain_len), 'starting from number', str(max_chain_num))
