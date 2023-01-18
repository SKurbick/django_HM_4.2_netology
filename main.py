#
# [-1, 0, 1, 2, 3] -> True
# [-1, 0, 1, 3, 4]) -> False
# [0, 1] -> True
# [1, 0] -> False

values = [0, 1]
len_val = len(values)
new_list = []

for item in range(len_val):
    print(item)
    new_v = values[0] + item
    new_list.append(new_v)
print(new_list == values)
print(new_list)
# new_list = [values[0] + i for i in range(len(values))]
# print(new_list == values)
# print(new_list)
#

n = [-1, 0, 1, 3, 4]
flag = True
for i in range(len(n) - 1):
    if n[i] + 1 != n[i + 1]:
        flag = False
# print(flag)

print(1 + 2)


