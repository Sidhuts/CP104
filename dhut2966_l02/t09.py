"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sidharth Dhutti
ID:      169062966
Email:  dhut2966@mylaurier.ca
__updated__ = "2023-09-14"
------------------------------------------------------------------------
"""
diameter_base = float(input())
height = float(input())
cost_per_cm2 = float(input())
num_containers = int(input())
radius = (diameter_base / 2)
pi = 3.14
area_circular_base = (pi * (radius**2))
area_outside = (2 * pi * radius * height)
surface_area = (area_circular_base + area_outside)
cost_per = (surface_area * cost_per_cm2)
cost_all = (surface_area * cost_per_cm2 * num_containers)
print(cost_per)
print(cost_all)