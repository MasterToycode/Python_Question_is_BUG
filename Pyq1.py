def modify_list(my_list):
    my_list.append(4)
    return

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # 输出结果为 [1, 2, 3, 4]


def assign_list(my_list):
    my_list = [1, 2, 3]
    return

my_list = [4, 5, 6]
assign_list(my_list)
print(my_list)  # 输出结果为 [4, 5, 6]
