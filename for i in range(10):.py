from math import * 

# First we need to prompt the user for a value of x.

# Define x as the the user input

x = float(input("Enter a value for x: "))

# If the user enters a value outside the 0 < x <= 2 range,
# a loop is created until the user enters a valid number

while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))

# Now we prompt the user to enter a tolerance value for our series expansion:

tolerance = float(input("Enter the tolerance value: "))

# I'm just going to set the first term seperate from the expanded series

series_term = (x - 1)  

approximate_ln = series_term  
k = 2  # Start from k = 2 for the next term

# Each series term alternates between + and - 
# Calculate the Taylor series until the term is less than the tolerance

while abs(series_term) > tolerance:
    series_term = ((-1) ** (k + 1)) * (((x - 1) ** k) / k)  # Calculate the kth term
    approximate_ln += series_term  # Add the nth term to the approximation
    k += 1  # Increment n for the next term

# Final output: 
print(f"The approximation of ln({x}) is {approximate_ln}")


