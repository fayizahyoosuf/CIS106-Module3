# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:49:43 2026

@author: shama
"""

ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print()
print("Stock Ticker:", ticker)
print("Amount Invested: ${:.2f}".format(amount_invested))
