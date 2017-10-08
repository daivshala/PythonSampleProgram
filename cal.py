#!/usr/bin/env python3
amount=float(input("Enter the amoount:"))
intrest=float(input("Enter the intrest:"))
period=int(input("Enter the period:"))
vlaue=0
year=1
while year <= period:
	value = amount + (intrest * amount)
	print("Year %d Rs. %.2f" % (year, value))
	amount = value
	year = year + 1


