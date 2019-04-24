"""Download flags of top 20 countries by population

asyncio + aiottp version

Sample run::

    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s

"""
# BEGIN FLAGS_ASYNCIO
import asyncio

import aiohttp  # <1>

from futures_test.flags import BASE_URL, save_flag, show, main   # <2>


async def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)  # <4> 异步发起请求
        image = await resp.read()  # <5> 异步下载请求内容
        return image


async def download_one(cc):  # <6>
    image = await get_flag(cc)  # <7>
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    # print(cc)
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()  # <8>
    to_do = {download_one(cc) for cc in sorted(cc_list)}  # <9> 生成器对象列表/set（）
    print(type(to_do))
    print(to_do)
    # print(to_do)
    wait_coro = asyncio.wait(to_do)  # <10> wait 也只能接受可迭代对象
    print(type(wait_coro))
    print(wait_coro)
    res, _ = loop.run_until_complete(wait_coro)  # <11>
    loop.close() # <12>
    # wait_coro.close()

    return len(res)


if __name__ == '__main__':
    main(download_many)
# END FLAGS_ASYNCIO






