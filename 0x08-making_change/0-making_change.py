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

    coins.sort(reverse=True)

    min_coins_needed = 0
    remaining_amount = total

    for coin in coins:
        if remaining_amount >= coin:
            num_coins = remaining_amount // coin
            min_coins_needed += num_coins
            remaining_amount -= num_coins * coin

    return min_coins_needed if remaining_amount == 0 else -1
