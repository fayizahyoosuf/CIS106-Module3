# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:49:35 2026

@author: shama
"""

last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm exam score: "))
final = float(input("Enter your final exam score: "))

total_exam_points = (midterm * 0.40) + (final * 0.60)

print()
print("Student Last Name:", last_name)
print("Total Exam Points: {:.2f}".format(total_exam_points))