import string


def Word_fun(path):
    try:
        # 打开文件并读取内容
        with open(path, "r") as text:
            # 将文本内容按空格分割成单词，并将每个单词转换为小写形式，同时去除单词两端的标点符号
            words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]

            # 将单词列表转换成集合，以获取独一无二的单词列表
            words_index = set(words)

            # 创建一个字典，以每个单词为键，记录该单词在文本中出现的次数为值
            counts_dict = {index: words.count(index) for index in words_index}

            # 将counts_dict声明为全局变量（但实际上此处声明为全局变量是多余的，因为它已经在函数内部定义了）
            global counts_dict
    except Exception as mistake:
        # 如果发生异常（如文件找不到），输出错误信息
        print("无法找到文件", mistake)


def Output(counts_dict):
    # 按照字典中各单词出现次数的降序排序，并输出每个单词及其出现次数
    for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
        print('{} -- {} 次'.format(word, counts_dict[x]))
