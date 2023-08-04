import json
import requests
import re
import time
from requests.exceptions import RequestException
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_html(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?board-img.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?主演：(.*?)</p>.*?releasetime.*?上映时间：(.*?)</p>.*?score.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '封面图': item[1],
            '电影名': item[2].strip(),
            '主演': item[3].strip(),
            '上映时间': item[4].strip(),
            '评分': item[5] + item[6]
        }

def write_to_file(content):
    try:
        with open('D:\不会编程\python\实验文件夹\实验文档.txt','a',encoding='utf-8') as f:
            print(type((json.dumps(content))))
            f.write(json.dumps(content,ensure_ascii=False)+'\n')
    except Exception:
        print('写入错误')

def main(offset):
    url = 'https://www.maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_html(html):
        print(item)
        write_to_file(item)


'''想象你是一位厨师，你有一本食谱，这个食谱是一个Python文件。当你要准备一道菜时，你会打开这个食谱，并根据上面的步骤和说明来进行烹饪。这个过程就类似于在Python中直接运行一个脚本。

现在，你是另一位厨师，你想借用之前那位厨师的烹饪技巧来制作一道菜。你并不需要知道那个厨师是怎么准备菜的，你只需要看到最后的成品。这时，你就可以将食谱文件导入到你的菜谱本中，以获得那道菜的成品。这个过程就类似于在Python中导入一个模块。

在Python中，if __name__ == '__main__':就像是食谱文件中的一部分，它表示：如果这个食谱是主菜单（主模块），那么执行这里的指令。但是如果这个食谱是其他菜谱的一部分（被导入为模块），那么不执行这里的指令。

这样做的好处是，当你需要运行整个食谱（直接执行脚本），你只需要打开这个文件（Python脚本），然后所有的指令都会被执行。而如果你只想借用其中的一部分烹饪技巧（导入为模块），你可以在其他地方导入这个文件，而不会让它执行整个食谱（避免重复执行）。
'''
if __name__ == '__main__':
    for i in range(10):
     main(offset=i*10)
     time.sleep(1)
