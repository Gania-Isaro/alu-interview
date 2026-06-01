"""
Minimum Operations

Given a file with a single 'H', you can only perform two operations:
1. Copy All: Copy all characters in the file
2. Paste: Paste the clipboard content

Find the minimum number of operations to result in exactly n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations to achieve exactly n H.

    This is a prime factorization problem. To multiply the current
    content by a factor m, we need m operations (1 Copy All +
    (m-1) Pastes).

    Therefore, the minimum operations equals the sum of all prime
    factors of n.

    Args:
        n: The target number of H characters

    Returns:
        The minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Find all prime factors and sum them
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
