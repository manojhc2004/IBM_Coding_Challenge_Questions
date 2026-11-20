"""
Problem Description: License Plate Formatting

Write a function that validates and reformats a given license plate string according to a specific set of rules. If the input fails any validation criteria, the function must return the string "INVALID".

Validation & Processing Rules

1. Allowed Characters:
	• The license plate can only contain alphanumeric characters (A-Z, a-z, 0-9).
	• Any other characters (such as spaces, symbols, or special characters) should be treated as invalid.
2. Uppercase Conversion:
	• All lowercase letters must be converted to uppercase.
3. Length Constraints:
	• The processed license plate must have between 2 and 10 characters, inclusive.
	• If the license plate has fewer than 2 characters or more than 10 characters after removing any invalid/extra formatting, it should be considered invalid.
4. Digit Count:
	• The license plate must contain at least one digit (0-9). If no digit is present, the plate is considered invalid.

Formatting Rules

A valid license plate must be formatted into groups of 2 or 3 characters separated by hyphens (-), based on its total alphanumeric length:
• If the length is divisible by 3: Split the string completely into groups of 3 characters each.
• If the length is not divisible by 3: Create as many groups of 3 characters as possible, ensuring that the last group has exactly 2 characters (and if necessary to avoid a single character remaining, the second-to-last group can also have 2 characters).

Examples:

• 9 characters: ABC123XYZ \(\rightarrow \) ABC-123-XYZ (All groups of 3)
• 8 characters: ABC123XY \(\rightarrow \) ABC-123-XY (Two groups of 3, last group of 2)
• 7 characters: ABC1234 \(\rightarrow \) ABC-12-34 (One group of 3, followed by two groups of 2)
"""
def format_plate(s):
    
    reformate = ""
    isdigit = False

    for ch in s:
        if ch.isdigit():
            isdigit = True
            reformate += ch
        elif ch.isascii() and ch.isalpha():
            reformate += ch.upper()
        else:
            return "INVALID"

    n = len(reformate)

    if n < 2 or n > 10 or not isdigit:
        return "INVALID"

    groups = []
    i = 0

    while i < n:
        remaining = n - i

        size = 2 if remaining == 4 else 3

        groups.append(reformate[i:i + size])
        i += size

    return "-".join(groups)


print(format_plate("abce2g"))