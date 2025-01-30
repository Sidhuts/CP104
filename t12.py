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
Total_sconds = int(input("Number of seconds: "))
Days = Total_sconds // 86400
Remaining_seconds = Total_sconds % 86400
Hours = Remaining_seconds // 3600
Remaining_seconds %= 3600
Mins = Remaining_seconds // 60
Secs = Remaining_seconds %60

print(f"Days: {Days}, Hours: {Hours}, Minutes: {Mins}, Seconds: {Secs}")
