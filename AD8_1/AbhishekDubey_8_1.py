# Import the necessary libraries
import math
import numpy as np
import pandas as pd
from datetime import datetime

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Using datetime module")
# Ask the user for their name
name = input("Please enter your name: ")

# Ask the user for their age
# We use int() to convert the input string to an integer
age = int(input("Please enter your age: "))

# Calculate the year the user was born
# We subtract the user's age from the current year
birth_year = datetime.now().year - age

# Print the result
# We use an f-string to insert the user's name and birth year into the message
print(f"Hello {name}, you were born in {birth_year}.")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# Using the math module
print("Using the math module:")

# Calculate the square root of 16
print("Square root of 16 is:", math.sqrt(16))

# Calculate the factorial of 5
print("Factorial of 5 is:", math.factorial(5))

# Calculate the natural logarithm of 2
print("Natural logarithm of 2 is:", math.log(2))

# Using the numpy module
print("\nUsing the numpy module:")

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Perform element-wise addition
print("Element-wise addition of 2:", arr + 2)

# Perform element-wise multiplication
print("Element-wise multiplication by 2:", arr * 2)

# Calculate the mean of the array
print("Mean of the array:", np.mean(arr))

# Using the pandas module
print("\nUsing the pandas module:")

# Create a pandas DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
})

# Perform addition using a DataFrame column
print("Addition using a DataFrame column:\n", df['A'] + df['B'])

# Perform multiplication using a DataFrame column
print("Multiplication using a DataFrame column:\n", df['A'] * df['B'])

# Calculate the mean of a DataFrame column
print("Mean of column 'A':", df['A'].mean())
