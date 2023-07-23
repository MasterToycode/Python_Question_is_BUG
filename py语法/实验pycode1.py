
def create_files():
    # 写入内容
    内容 = "这是一个简单的例子。\n你可以在这个文件中添加更多内容。"
    count = 1  # 从1开始，用于作为文件名的一部分

    while count <= 10:
        文件名 = 'D:/不会编程/python/py语法/'+ str(count) + '.txt'  # 将数字转换为字符串
        try:
            with open(文件名, "w") as 文件对象:
                文件对象.write(内容)
                print("成功写入文件！", 文件名)
                count = count + 1
        except Exception as 错误:
            print("创建文件错误", 错误)
        else:
            print("没有发生异常。")
        finally:
            print("无论是否发生异常，都会执行finally块。")

create_files()


try:

    # 可能会引发异常的代码块
    with 上下文表达式 as 变量:
    # 在此处执行需要使用资源的代码块

    # 在这里编写可能会出现异常的代码
except 异常类型1:
    # 处理异常类型1的代码块
except 异常类型2:
    # 处理异常类型2的代码块
# 可以继续添加更多的except块来处理其他异常类型
#except Exception as 错误是一个通用的异常捕获块，它能够捕获继承自Exception类的所有异常。
#Exception是Python中所有内置异常类的基类，因此它能够捕获绝大多数常见的异常情况。
else:
    # 可选：如果没有发生异常，执行此处的代码块
finally:
    # 可选：无论是否发生异常，最终都会执行此处的代码块



