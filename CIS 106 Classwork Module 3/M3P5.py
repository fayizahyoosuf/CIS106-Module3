# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:22:08 2026

@author: shama
"""

radius = float(input("Enter the radius of the circle: "))

pi = 3.14

area = pi * radius * radius
perimeter = 2 * pi * radius

print()
print("Area: {:.2f}".format(area))
print("Perimeter: {:.2f}".format(perimeter))