# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:42:07 2026

@author: shama
"""

make = input("Enter the make: ")
model = input("Enter the model: ")
msrp = float(input("Enter the MSRP: "))
discount = float(input("Enter the discount as a decimal: "))

amount_off = msrp * discount
discounted_price = msrp - amount_off

print("Make:", make)
print("Model:", model)
print("MSRP: $%.2f" % msrp)
print("Discount: %.2f" % discount)
print("Amount Off: $%.2f" % amount_off)
print("Discounted Price: $%.2f" % discounted_price)