# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peyton Kocher
# Section:      559
# Assignment:   Lab 6.15
# Date:         26 September 2024


from math import *

# First we need to prompt the user for a value of x.

# Define x as the the user input

x = float(input("Enter a value for x: "))

# If the user enters a value outside the 0 < x <= 2 range,
# a loop is created until the user enters a valid number

while x <= 0 or x > 2: 
    x = float(input("Out of range! Try again: "))

# Now we prompt the user to enter a tolerance value for our series expansion:

tolerance = float(input("Enter the tolerance: "))

# If I let this first term stay alone, I can add the series values all together at the end in a nice simple way:
k = 1
series_term = (x - 1)  # first term
approximate_ln = series_term  # when k = 1 

# Creating a loop so that the terms keep going until the Taylor series is less than the tolerate
# Since we don't know how long it will take to reach less than tolerance, use a while loop
# Start from k = 2 for next term 

while series_term > tolerance:
    series_term = (-1 ** (k - 1)) * (((x - 1) ** (k)) / k)
    approximate_ln += series_term  # adds to the approximation
    k += 1   # Increments k for the next term

exact_ln = log(x)

# Final output lines: 

print(f"ln({x}) is approximately {approximate_ln}")
print(f"ln({x}) is exactly {exact_ln}")
print(f"The difference is {abs(exact_ln - approximate_ln)}")