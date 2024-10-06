# list = ["cherries", "apple", "peach", "banana"]
# list.append("strawberries")
# list.remove("banana")
# x = list.pop(2)

# if "strawberries" in list:
#     print("strawberry is present")

# for fruit in list:
#     print(fruit)

# for i in range (len(list)):
#     list[i]

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range (len(list)):
#     print(list[i][2])

for i in range (len(list)):
    for j in range (len(list[0])):
        print(list[i][j])

# print(list[2])