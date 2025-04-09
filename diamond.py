n = int(input("Enter a number: "))
rows = n * 2 - 1
for i in range(1, rows + 1):
    if i <= n:
        spaces = n - i
        stars = 2 * i - 1
    else:
        spaces = i - n
        stars = 2 * (rows - i + 1) - 1

    print(" " * spaces + "*" * stars)
# This code generates a diamond pattern based on the input number.
# The number of rows in the diamond is calculated as n * 2 - 1.
# The first half of the diamond is created by increasing the number of stars
# and decreasing the number of spaces, while the second half is created by
# decreasing the number of stars and increasing the number of spaces.
# The spaces and stars are calculated based on the current row number.
# The print statement formats the output to create the diamond shape.
# The diamond pattern is symmetric, with the widest part in the middle.
# The pattern is centered by using spaces before the stars.
# The code uses a for loop to iterate through each row of the diamond.
# The spaces are calculated as the difference between the total number of rows
# and the current row number.
# The stars are calculated based on the current row number.
# The code uses string multiplication to create the required number of spaces
# and stars for each row.
# The diamond pattern is printed to the console using the print function.
# The code is efficient and works for any positive integer input.
# The diamond pattern is a common exercise in programming to practice loops
# and string manipulation.
# The code can be modified to create different shapes by changing the
# calculations for spaces and stars.
# The diamond pattern can also be created using other characters instead of
# stars by replacing the "*" in the print statement with a different character.
# The code can be easily adapted to create different sizes of diamonds by
# changing the input number.
# The diamond pattern can also be created using different symbols or characters
# by modifying the print statement.
# The code can be extended to include additional features such as color or
# animation by using libraries such as colorama or curses.
# The diamond pattern can be used in various applications such as graphics,
# user interfaces, and games.
# The code is a simple and effective way to create a diamond pattern using
# basic programming concepts such as loops, conditionals, and string
# manipulation.
# The diamond pattern can be used as a fun exercise for beginners to practice
# their programming skills and learn about loops and string formatting. 
