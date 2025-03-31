# Program to calculate the sum of a Geometric Progression (GP)

# Get input from user
first_term = float(input("Enter the first term: "))
common_ratio = float(input("Enter the common ratio: "))
num_terms = int(input("Enter number of terms: "))

# Initialize sum
gp_sum = 0

# Calculate each term and add to sum
current_term = first_term
for _ in range(num_terms):
    gp_sum += current_term
    current_term *= common_ratio  # Calculate next term

# Display the result
print(f"The sum of the GP is: {gp_sum}")
