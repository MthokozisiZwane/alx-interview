#!/usr/bin/python3
"""
Dtermines the winner in a game where prime numbers along with their
multiples are removed from set one player at a time.
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        prime_numb = [True] * (n + 1)
        prime_numb[0] = prime_numb[1] = False
        p = 2
        while p ** 2 <= n:
            if prime_numb[p]:
                for i in range(p ** 2, n + 1, p):
                    prime_numb[i] = False
            p += 1
        return [p for p in range(2, n + 1) if prime_numb[p]]

    def is_prime(n):
        if n < 2:
            return False
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                return False
        return True

    def play_game(n):
        prime_numb = sieve_of_eratosthenes(n)
        remaining = set(range(1, n + 1))
        winner = None
        while remaining:
            if not any(is_prime(num) for num in remaining):
                break
            if winner == 'Maria':
                winner = 'Ben'
            else:
                winner = 'Maria'
            prime = next((num for num in prime_numb if num in remaining), None)
            remaining -= set(range(prime, n + 1, prime))
        return winner

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = play_game(n)
        if winner:
            wins[winner] += 1
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
