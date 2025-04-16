original_number = input("Enter a positive integer: ")

reversed_number = 0
number_of_digits = 0
truncated_number = original_number

for number in original_number:
    number_of_digits += 1

for number in range(number_of_digits):
    last_digit = int(truncated_number) % 10
    print(f"Digit {last_digit}")
    reversed_number = reversed_number * 10 + last_digit
    print(f"Reversed number {reversed_number}")
    truncated_number = int(truncated_number) // 10
    print(f"Numbers {truncated_number}")

print(f"reversed_number {reversed_number}")
print(f"original_number {original_number}")

print(f"type: reversed_number {type(reversed_number)}")
print(f"type: original_number {type(original_number)}")

if int(reversed_number) == int(original_number):
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
