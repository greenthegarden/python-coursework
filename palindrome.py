numbers = input("Enter a positive integer: ")
if numbers.isdigit():
    numbers = str(numbers)  
else:   
    print("Invalid input. Please enter a positive integer.")
    exit()

if numbers == numbers[::-1]:
    print(f"{numbers} is a palindrome.")
else:
    print(f"{numbers} is not a palindrome.")


