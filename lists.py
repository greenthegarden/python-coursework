list1 = [50, 60, 70, 80]
list2 = [10, 20, 30, 40]
list3 = [1, 2, 3, 4]
list4 = [5, 6, 7, 8]
list5 = [9, 10, 11, 12]

all_lists = [list1, list2, list3, list4, list5]

print("All lists:")
for lst in all_lists:
    print(lst)

result = [[], [], [], []]

for i in range(4):
    for lst in all_lists:
        result[i].append(lst[i])

print(result)

print(all_lists)
