#!/usr/bin/python3


def sieve_of_eratosthenes(max_n):
    """ Generates a list of primes up to max_n using the
    Sieve of Eratosthenes
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes, is_prime


def calculate_winning_positions(max_n, primes, is_prime):
    """ Calculate winning positions for each number of primes up to max_n """
    winning = [False] * (max_n + 1)
    for num in range(2, max_n + 1):
        for prime in primes:
            if prime > num:
                break
            if not winning[num - prime]:
                winning[num] = True
                break
    return winning


def isWinner(x, nums):
    """ count player wins"""
    max_n = max(nums)
    primes, is_prime = sieve_of_eratosthenes(max_n)
    winning = calculate_winning_positions(max_n, primes, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if winning[n]:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
