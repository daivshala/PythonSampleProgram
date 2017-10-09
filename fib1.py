#!/usr/bin/env python3
# Fibonacci series using while loop and end space string
a, b = 0, 1
while b < 100:
	print(b, end=' ')
	a, b = b, a + b
