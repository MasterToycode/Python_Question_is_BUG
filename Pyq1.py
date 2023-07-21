在 Python 中，函数参数的传递方式是按值传递，但对于可变类型的参数（例如列表、字典等），函数内部的修改会影响到原始对象。


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
