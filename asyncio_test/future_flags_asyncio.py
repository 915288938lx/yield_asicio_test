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


@asyncio.coroutine  # <3>
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.ClientSession().get(url)  # <4>
    image = yield from resp.read()  # <5>
    return image


@asyncio.coroutine
def download_one(cc):  # <6>
    image = yield from get_flag(cc)  # <7>
    # print(type(image))
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    # print(cc)
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()  # <8>
    to_do = [download_one(cc) for cc in sorted(cc_list)]  # <9> 生成器对象列表
    # print(to_do)
    wait_coro = asyncio.wait(to_do)  # <10>
    print('sajdsklja;lkj;kafdj;alk',wait_coro)
    res, _ = loop.run_until_complete(wait_coro)  # <11>
    loop.close() # <12>
    # wait_coro.close()

    return len(res)


if __name__ == '__main__':
    main(download_many)
# END FLAGS_ASYNCIO
"""
download_many()
    download_one()
        yield from get_flag(cc) # 协程
            get_flag()
                yield from aiohttp.ClientSession().get(url) # 协程
                    to_do_list()
                        asyncio.wait(to_do_list())
                            run_until_complete(wait())
                
        



"""