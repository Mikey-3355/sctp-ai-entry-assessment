# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Capitalise both names, then return "lastName, firstName" format
    # .title() handles mixed case inputs like "bob" → "Bob"
    return f"{lastName.title()}, {firstName.title()}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # Take the first character of each name, uppercase it, and join with dots
    first_init = firstName[0].upper()
    last_init = lastName[0].upper()
    return f"{first_init}.{last_init}."


# Task 3:
# Call both functions with the following inputs and print each result:
print(formatName("Alice", "Tan"))     # Expected: "Tan, Alice"
print(formatName("bob", "lim"))       # Expected: "Lim, Bob"
print(formatInitials("Alice", "Tan"))  # Expected: "A.T."
print(formatInitials("bob", "lim"))    # Expected: "B.L."