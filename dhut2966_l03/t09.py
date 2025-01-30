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
#imports
sweatband = float(input("Enter sweatband cost: $"))
pants = float(input("Enter pants cost: $"))
jacket = float(input("Enter jacket cost: $"))

total = sweatband + pants  + jacket
print()

print("Clothes      Cost")
print(f"Sweatband    ${sweatband:6.2f}")
print(f"Pants        ${pants:6.2f}")
print(f"Jacket       ${jacket:6.2f}")
print(f"Total        ${total:6.2f}")