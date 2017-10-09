#!/usr/bin/env python3
# Multiplication Table using nested while loop 
i = 1
print("-" * 50)
while i < 11:
	n = 1
	while n <= 10:
        	print("%4d" % (i * n), end=' ')
        	n += 1
	print()
	i += 1
print("-" * 50)

