#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
  the fewest number of coins needed to meet a given
  amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins
    #   for each amount from 0 to total.
    # Initialize all values to a large number (infinity)
    #   initially.
    dp = [float('inf')] * (total + 1)

    # For 0 total, the fewest number of coins needed is 0.
    dp[0] = 0

    # Iterate through each coin denomination.
    for coin in coins:
        # Update the dp array for each possible amount from
        #   the coin value up to total.
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot
    #  be met by any combination of coins.
    if dp[total] == float('inf'):
        return -1

    return dp[total]
