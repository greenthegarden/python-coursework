# Sequence
# 0 1 1 2 3 5 8 13 21 34 55 89
# a
#   a
#     a b
#     a+b

num = int(input("Enter a number: "))

for i in range(num):
    if i == 0:
        a = 0
    elif i == 1:
        a = 1
        b = a
    else:
        a = b
        b = a + b
    solution = a
    print(solution, end=" ")
