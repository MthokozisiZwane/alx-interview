#!/usr/bin/python3
"""
Module for making change.
"""
import math


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

    min_coins_n = [math.inf] * (total + 1)
    min_coins_n[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_coins_n[amount] = min(min_coins_n[amount],
                                          min_coins_n[amount - coin] + 1)

    return min_coins_n[total] if min_coins_n[total] != math.inf else -1
