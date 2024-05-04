#!/usr/bin/python3
"""
Module for making change.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): The targeted total amount.

    Returns:
        int: Fewest number of coins needed to meet the total, or
        -1 if not possible.
    """
    if total <= 0:
        return 0

    list_coins = [float('inf')] * (total + 1)
    list_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            list_coins[amount] = min(list_coins[amount], list_coins[amount
                                     - coin] + 1)

    return list_coins[total] if list_coins[total] != float('inf') else -1
