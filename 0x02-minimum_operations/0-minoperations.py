#!/usr/bin/python3
""" 0x02-minimum operations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operation needed to return in exactly n H character
    """
    # all outputs should be atleast 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller values that evenly-divide n
            root -= 1
        # increment root until it evenly-divide n
        root += 1
    return ops
