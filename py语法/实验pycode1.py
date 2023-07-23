
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





