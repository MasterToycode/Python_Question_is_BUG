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



''' string.punctuation 是Python中内置的一个字符串，它包含了所有标点符号的字符。例如，string.punctuation 的值是："!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"。
raw_word 是一个字符串，表示从文本中读取出的原始单词，可能包含标点符号。
strip() 是字符串方法，它用于去除字符串两端的指定字符，默认情况下会去除字符串两端的空格。
string.punctuation 作为strip()的参数，意味着我们希望去除单词两端的所有标点符号字符。

lambda 是Python中的一个关键字，用于创建匿名函数。所谓匿名函数，是指没有具体名称的小型函数，它通常用于简单的表达式或函数体较短的情况下。
在代码中，lambda x: counts_dict[x] 是一个匿名函数，其中 x 是参数，counts_dict[x] 是返回值。
这个lambda函数的作用是，给定一个参数x（在这里实际上是单词），返回该单词在counts_dict字典中对应的值，即该单词在文本中出现的次数。
在sorted函数中，我们使用了key参数来指定排序的关键字，这里就用到了lambda函数，帮助sorted函数确定按照哪个规则进行排序。
'''
lambda arguments: expression
'''
lambda 是关键字，表示声明一个匿名函数。
arguments 是函数的参数，可以是多个，但在匿名函数中通常用于简单的单个参数。
expression 是函数的返回值，通常是一个简单的表达式，计算结果将作为函数的返回值。
'''
