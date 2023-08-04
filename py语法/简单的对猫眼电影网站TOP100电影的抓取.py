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

if __name__ == '__main__':
    for i in range(10):
     main(offset=i*10)
     time.sleep(1)
