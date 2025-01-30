"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sidharth Dhutti
ID:      169062966
Email:  dhut2966@mylaurier.ca
__updated__ = "2023-09-20"
------------------------------------------------------------------------
"""
#imports
large_dogs = int(input("Number of large dogs groomed: "))
small_dogs = int(input("Number of small dogs groomed: "))
LDP = 75
SDP = 50
print()
price = large_dogs * LDP + small_dogs * SDP

print("Total earned for the day: $ ", price)