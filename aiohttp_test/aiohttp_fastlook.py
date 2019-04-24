import aiohttp
import asyncio
import async_timeout
import json

HEADERS = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "Content-Type": "application/json",
    "Host": "gs.amac.org.cn",
    "Origin": "http://gs.amac.org.cn",
    "Referer": "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
    "X-Requested-With": "XMLHttpRequest"
}
PAYLOAD = {}
REQUEST_PARAMETERS = {
    'rand': '0.034480063759529056',
    'page': '0',
    'size': '20'
}

def get_url(page_num): # 返回请求参数
    REQUEST_PARAMETERS = {
        'rand': '0.034480063759529056',
        'page': page_num,
        'size': '100'
    }
    request_params =  REQUEST_PARAMETERS
    return request_params




async def fetch(session, url):  # 类似于@coroutine
    with async_timeout.timeout(10):  # 超时时间
        async with session.post(url, params=REQUEST_PARAMETERS, data=json.dumps(PAYLOAD),
                                headers=HEADERS) as response:  # 发送非表单数据给服务器，都必须先序列化，比如json数据，既可以用data=json.dumps(PAYLOAD)，又可以用json=PAYLOAD, 如果是发送表单数据，则直接data=payload即可，params是请求参数，会放到链接处
            print(response.status)
            print(response.url)
            with open('a.html', 'wb') as fp:  # await 类似于yield from
                while True:
                    chunk = await response.content.read(10)
                    if not chunk:
                        break
                    fp.write(chunk)
                print('write file success!')


async def main(url):
    async with aiohttp.ClientSession() as session:
        await fetch(session, url)

url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager?'
loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))

from collections import deque
dq = deque([1,2,3],maxlen=10)


import time
t = time.clock()
time.sleep(3)
tt = time.clock()
ttt = tt-t
print(int(ttt)   )
