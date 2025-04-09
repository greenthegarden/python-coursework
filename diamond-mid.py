n = int(input("Enter a number: "))
size = n * 2 - 1
mid = n - 1
print(f"n: {n}, size: {size}, mid: {mid}")
print("Diamond Pattern:")
for row in range(size):
    for col in range(size):
        print(f"(mid - row): {mid - row}, (mid - col): {mid - col}")
        print(f"abs(mid - row): {abs(mid - row)}, abs(mid - col): {abs(mid - col)}, mid: {mid}")
        print()
for row in range(size):
    for col in range(size):
        if abs(mid - row) + abs(mid - col) <= mid:
            print("*", end="")
        else:
            print("-", end="")
    print()
